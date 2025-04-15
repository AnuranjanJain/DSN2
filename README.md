# Cardio Guide - Heart Disease Risk Predictor

An AI-powered web application that predicts heart disease risk based on medical and lifestyle factors.

## Overview

Cardio Guide is a Flask-based web application that utilizes machine learning to predict an individual's risk of heart disease. The application analyzes various health parameters to provide a personalized risk assessment and recommendations.

![Cardio Guide Screenshot](screenshot.png)

## Features

- **Heart Risk Assessment**: Get a personalized heart disease risk prediction based on medical and lifestyle inputs
- **Interactive UI**: User-friendly interface with multi-step form for data input
- **Visualizations**: Clear graphical representation of risk factors and prediction results
- **Health Tips**: Comprehensive cardiovascular health recommendations
- **Responsive Design**: Works on various devices and screen sizes

## Technical Details

- **Framework**: Flask (Python)
- **Machine Learning**: Random Forest Classifier with scikit-learn
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Training Dataset**: Comprehensive heart disease dataset with 10,000+ records
- **Model Accuracy**: 99.2% on test data

## Installation and Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cardio-guide.git
   cd cardio-guide
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Train the model (skip if using pre-trained model):
   ```
   python train_model.py
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Files and Directory Structure

- `app.py`: Main Flask application
- `train_model.py`: Script to train the machine learning model
- `model1.pk1`: Trained machine learning model file
- `templates/`: HTML templates for the web pages
- `static/`: CSS, JavaScript, and image files
- `cleaned_heart_disease_dataset.csv`: Dataset used for model training

## Model Training

The model is trained on a comprehensive heart disease dataset that includes various factors such as:
- Age, gender, cholesterol levels
- Blood pressure measurements
- Medical history (diabetes, family history)
- Lifestyle factors (smoking, diet, physical activity)

## Future Improvements

- User accounts for saving assessments over time
- More detailed analysis of risk factors
- Mobile application version
- Integration with wearable health devices

## License

This project is licensed under the MIT License - see the LICENSE file for details.
