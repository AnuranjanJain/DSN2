from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import pandas as pd
import pickle
import json

app = Flask(__name__)

# Load the trained AI model
print("Loading model...")
try:
    with open('model1.pk1', 'rb') as f:
        model_data = pickle.load(f)
        pipeline = model_data['pipeline']
        features = model_data['features']
        categorical_cols = model_data['categorical_cols']
        numerical_cols = model_data['numerical_cols']
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    # Default values in case model loading fails
    pipeline = None
    features = []
    categorical_cols = []
    numerical_cols = []

# Load feature statistics for visualization
try:
    df = pd.read_csv('cleaned_heart_disease_dataset.csv')
    feature_stats = {
        'age': {
            'min': int(df['age'].min()),
            'max': int(df['age'].max()),
            'mean': int(df['age'].mean())
        },
        'cholesterol': {
            'min': int(df['cholesterol'].min()),
            'max': int(df['cholesterol'].max()),
            'mean': int(df['cholesterol'].mean())
        },
        'diabetes': {
            'percent': round(df['diabetes'].mean() * 100, 1)
        },
        'smoking': {
            'percent': round(df['smoking'].mean() * 100, 1)
        },
        'heart_disease': {
            'percent': round(df['heart_disease'].mean() * 100, 1)
        }
    }
    print("Feature stats loaded successfully!")
except Exception as e:
    print(f"Error loading feature stats: {e}")
    feature_stats = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html', features=features, categorical_cols=categorical_cols)

@app.route('/about')
def about():
    return render_template('about.html', stats=feature_stats)

@app.route('/health_tips')
def health_tips():
    return render_template('health_tips.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if pipeline is None:
            raise ValueError("Model not loaded correctly")
        
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
        
        # Fill missing features with default values
        for feature in features:
            if feature not in feature_dict:
                feature_dict[feature] = 0.0 if feature not in categorical_cols else "Average"
        
        # Convert to DataFrame to ensure correct column order
        input_df = pd.DataFrame([feature_dict])
        
        # Make prediction using the pipeline
        prediction_prob = pipeline.predict_proba(input_df)[0][1]
        prediction_class = pipeline.predict(input_df)[0]
        
        # Calculate risk level based on probability
        if prediction_prob < 0.3:
            risk_level = "Low"
            color = "green"
        elif prediction_prob < 0.7:
            risk_level = "Medium"
            color = "orange"
        else:
            risk_level = "High"
            color = "red"
        
        # Get feature importances for display
        # Since the pipeline changes the features, we'll use the top input features
        top_features = ["age", "cholesterol", "systolic_bp", "diastolic_bp", "obesity_bmi"]
        top_values = [feature_dict.get(f, 0) for f in top_features]
        
        # Prepare visualization data
        viz_data = {
            'top_features': top_features,
            'values': top_values
        }
        
        # Return prediction result
        return render_template('result.html', 
                               prediction=round(prediction_prob * 100, 2),
                               prediction_class=int(prediction_class),
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
        
        # Return analysis
        return jsonify({
            'status': 'success',
            'message': 'Analysis complete',
            'data': {
                'input': data,
                'analysis': 'Placeholder for analysis'
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
