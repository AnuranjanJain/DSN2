from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import pandas as pd
import json
import os
import re
import random
from model import FraminghamModel, get_model_features, predict
import chatbot_responses as cr

# Create Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('config.DevelopmentConfig')

# Initialize the model
print("Loading model...")
try:
    model = FraminghamModel()
    model_path = 'model1.pk1'  # Use model1.pk1 as the primary model file
    model.model_path = model_path
    
    if model.load() or os.path.exists(model_path):
        print("Model loaded successfully!")
        # Get model features for form and prediction
        model_features = get_model_features()
        features = model_features['features']
        categorical_cols = model_features['categorical_cols']
        numerical_cols = model_features['numerical_cols']
    else:
        print("Model not found, training a new one...")
        success, metrics = model.train()
        if success:
            print(f"Model trained successfully with metrics: {metrics}")
            # Save with the specific filename
            model.save(model_path)
            # Get model features for form and prediction
            model_features = get_model_features()
            features = model_features['features']
            categorical_cols = model_features['categorical_cols']
            numerical_cols = model_features['numerical_cols']
        else:
            print("Failed to train model")
            features = []
            categorical_cols = []
            numerical_cols = []
except Exception as e:
    print(f"Error initializing model: {e}")
    # Default values in case model initialization fails
    features = []
    categorical_cols = []
    numerical_cols = []

# Load feature statistics for visualization
try:
    df = pd.read_csv('framingham.csv')
    feature_stats = {
        'age': {
            'min': int(df['age'].min()),
            'max': int(df['age'].max()),
            'mean': int(df['age'].mean())
        },
        'tot_chol': {
            'min': int(df['totChol'].min()),
            'max': int(df['totChol'].max()),
            'mean': int(df['totChol'].mean())
        },
        'diabetes': {
            'percent': round(df['diabetes'].mean() * 100, 1)
        },
        'current_smoker': {
            'percent': round(df['currentSmoker'].mean() * 100, 1)
        },
        'heart_disease': {
            'percent': round(df['TenYearCHD'].mean() * 100, 1)
        }
    }
    print("Feature stats loaded successfully!")
except Exception as e:
    print(f"Error loading feature stats: {e}")
    feature_stats = {}

# Main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html', features=features, categorical_cols=categorical_cols)

@app.route('/about')
def about():
    # Get model metrics if available
    metrics = None
    try:
        with open(model_path, 'rb') as f:
            import pickle
            model_data = pickle.load(f)
            if 'metrics' in model_data:
                metrics = model_data['metrics']
    except:
        pass
    
    return render_template('about.html', stats=feature_stats, metrics=metrics)

@app.route('/health_tips')
def health_tips():
    return render_template('health_tips.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        # Create a feature dictionary with proper data types
        feature_dict = {}
        
        # Process form data
        for key in request.form:
            if key in features:
                # Check if the column is categorical
                if key in categorical_cols:
                    # Store as string
                    feature_dict[key] = request.form[key]
                else:
                    # Convert to float if numerical
                    try:
                        feature_dict[key] = float(request.form[key])
                    except ValueError:
                        # If conversion fails, use 0 as a fallback
                        feature_dict[key] = 0.0
        
        # Make prediction using the model
        result = predict(feature_dict)
        prediction_prob = result['risk_score']
        prediction_class = result['risk_class']
        risk_level = result['risk_level']
        
        # Determine color based on risk level
        if risk_level == "Low":
            color = "green"
        elif risk_level == "Medium":
            color = "orange"
        else:
            color = "red"
        
        # Get top features for display
        top_features = ["age", "tot_chol", "sys_bp", "dia_bp", "bmi"]
        top_values = [feature_dict.get(f, 0) for f in top_features]
        
        # Prepare visualization data
        viz_data = {
            'top_features': top_features,
            'values': top_values
        }
        
        # Return prediction result
        return render_template('result.html', 
                               prediction=round(prediction_prob * 100, 2),
                               prediction_class=prediction_class,
                               risk_level=risk_level,
                               color=color,
                               viz_data=json.dumps(viz_data),
                               input_data=feature_dict)
                             
    except Exception as e:
        import traceback
        print(f"Prediction error: {e}")
        traceback.print_exc()
        return render_template('result.html', error=str(e))

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        # Get user input
        data = request.json
        
        # Use our model to analyze the data
        result = predict(data)
        
        # Return analysis
        return jsonify({
            'status': 'success',
            'message': 'Analysis complete',
            'data': {
                'input': data,
                'analysis': result
            }
        })
    except Exception as e:
        app.logger.error(f"Error in /api/analyze: {e}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': 'An internal error occurred. Please try again later.'
        }), 500

# Direct API endpoint for health assistant
@app.route('/api/health-assistant', methods=['POST'])
def health_assistant_api():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({
                'status': 'error',
                'message': 'Empty message received'
            }), 400
        
        user_message = user_message.lower().strip()
        
        # Check for exact match first
        if user_message in cr.QUESTION_ANSWERS:
            return jsonify({
                'status': 'success',
                'response': cr.QUESTION_ANSWERS[user_message]
            })
        
        # Check for random health tip request
        if re.search(r'\b(tip|advice|suggestion)\b', user_message):
            return jsonify({
                'status': 'success',
                'response': random.choice(cr.HEALTH_TIPS)
            })
        
        # Pattern matching for common questions
        for pattern, response in cr.PATTERN_RESPONSES.items():
            if re.search(pattern, user_message):
                return jsonify({
                    'status': 'success',
                    'response': response
                })
        
        # Default response if no patterns match
        return jsonify({
            'status': 'success',
            'response': cr.DEFAULT_RESPONSE
        })
        
    except Exception as e:
        app.logger.error(f"Error in /api/health-assistant: {e}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': 'An internal error occurred. Please try again later.'
        }), 500

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', False))
