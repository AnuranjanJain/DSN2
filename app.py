from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import pandas as pd
import json
import os
import random
import re
from model import FraminghamModel, get_model_features, predict

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
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

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
        
        # Simple exact question matching
        question_answers = {
            "how can i lower my cholesterol naturally": "To lower cholesterol naturally: eat heart-healthy foods like oats, fatty fish, nuts, and foods rich in soluble fiber. Exercise regularly (aim for 30 minutes daily), lose weight if needed, quit smoking, and reduce alcohol consumption. Consider plant sterols and fiber supplements under medical guidance.",
            
            "what exercises are best for heart health": "The best exercises for heart health include: 1) Aerobic activities like walking, jogging, cycling, or swimming (150 minutes/week), 2) Interval training which alternates intense activity with recovery periods, 3) Strength training with weights or resistance bands (2-3 times weekly), and 4) Flexibility exercises. Always start gradually and consult a doctor if you have existing heart conditions.",
            
            "what does systolic and diastolic blood pressure mean": "Blood pressure readings have two numbers: Systolic (the top number) measures the pressure in your arteries when your heart beats. Diastolic (the bottom number) measures the pressure in your arteries when your heart rests between beats. Normal blood pressure is below 120/80 mmHg. High blood pressure increases heart disease risk and often has no symptoms.",
            
            "what are the main risk factors for heart disease": "Major heart disease risk factors include: age (45+ for men, 55+ for women), family history, high blood pressure, high cholesterol, smoking, diabetes, obesity, physical inactivity, unhealthy diet, excessive alcohol, and chronic stress. Some factors can't be changed, but many can be managed with lifestyle modifications and appropriate medical care."
        }
        
        # Check for exact match first
        if user_message in question_answers:
            return jsonify({
                'status': 'success',
                'response': question_answers[user_message]
            })
        
        # Pattern matching for common questions
        if re.search(r'cholesterol', user_message):
            return jsonify({
                'status': 'success',
                'response': "To lower cholesterol naturally: eat heart-healthy foods (oats, fatty fish, nuts), exercise regularly, lose weight if needed, quit smoking, and reduce alcohol consumption. Consider plant sterols and fiber supplements under medical guidance."
            })
        
        if re.search(r'exercise|workout', user_message):
            return jsonify({
                'status': 'success',
                'response': "The best exercises for heart health include aerobic activities (walking, jogging, cycling, swimming), interval training, and strength training. Aim for at least 150 minutes of moderate activity per week, spread across most days."
            })
            
        if re.search(r'blood pressure|hypertension', user_message):
            return jsonify({
                'status': 'success',
                'response': "Blood pressure has two numbers: Systolic (top) measures pressure during heartbeats, while diastolic (bottom) measures pressure between beats. Normal is below 120/80 mmHg. High blood pressure increases heart disease risk and often has no symptoms."
            })
            
        if re.search(r'diet|food|eat', user_message):
            return jsonify({
                'status': 'success',
                'response': "A heart-healthy diet includes fruits, vegetables, whole grains, lean protein, fish rich in omega-3s, nuts, and healthy oils. Limit saturated fats, trans fats, sodium, added sugars, and processed foods. The Mediterranean and DASH diets are excellent for heart health."
            })
            
        if re.search(r'heart.*(disease|attack|risk)', user_message):
            return jsonify({
                'status': 'success',
                'response': "Major heart disease risk factors include high blood pressure, high cholesterol, smoking, diabetes, obesity, physical inactivity, and family history. Signs of heart attack may include chest pain/pressure, shortness of breath, and pain radiating to the arm, jaw, or back. If you suspect a heart attack, seek emergency help immediately."
            })
            
        if re.search(r'(hi|hello|hey)', user_message):
            return jsonify({
                'status': 'success',
                'response': "Hello! I'm your Cardio Guide Health Assistant. I can help answer questions about heart health, risk factors, and lifestyle changes. How can I assist you today?"
            })
            
        if re.search(r'(thank you|thanks)', user_message):
            return jsonify({
                'status': 'success',
                'response': "You're welcome! Feel free to ask any other questions about heart health. I'm here to help."
            })
            
        if re.search(r'heart.*(health|lifestyle)', user_message):
            return jsonify({
                'status': 'success',
                'response': "A heart-healthy lifestyle includes: 1) Regular physical activity (150+ minutes weekly), 2) Balanced diet rich in fruits, vegetables, whole grains, and lean proteins, 3) Limited sodium, saturated fat, and added sugars, 4) No smoking, 5) Limited alcohol, 6) Healthy weight maintenance, 7) Stress management, and 8) Regular health checkups."
            })
        
        # Default response if no patterns match
        return jsonify({
            'status': 'success',
            'response': "I'm your heart health assistant. I can answer questions about heart disease, cholesterol, blood pressure, exercise, and heart-healthy diets. How can I help you with your cardiovascular health today?"
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
