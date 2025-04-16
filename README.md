# Cardio Guide - Heart Disease Risk Predictor

An AI-powered web application that predicts 10-year heart disease risk based on the Framingham Heart Study model.

## Overview

Cardio Guide is a Flask-based web application that utilizes machine learning to predict an individual's risk of coronary heart disease over the next 10 years. The application analyzes various health parameters using the Framingham Heart Study model to provide a personalized risk assessment and recommendations.

## Features

- **Heart Risk Assessment**: Personalized 10-year CHD risk prediction based on validated Framingham model parameters
- **Interactive UI**: User-friendly interface with multi-step form organized by demographic, lifestyle, medical history, and measurement data
- **Detailed Results**: Clear visualization of risk factors with comprehensive breakdown of input parameters and their impact
- **Health Tips**: Evidence-based cardiovascular health recommendations
- **About the Model**: Informative page about the Framingham Heart Study and model performance metrics
- **Responsive Design**: Works seamlessly on various devices and screen sizes

## Technical Details

- **Framework**: Flask (Python)
- **Machine Learning**: Random Forest Classifier with scikit-learn
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Training Dataset**: Framingham Heart Study dataset
- **Model File**: Pre-trained model (model1.pk1)

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

3. Train the model (optional - pre-trained model included):
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

- `app.py`: Main Flask application and routes
- `model.py`: Framingham model implementation and prediction logic
- `train_model.py`: Script to train and save the Framingham model
- `model1.pk1`: Pre-trained Framingham heart disease model
- `config.py`: Application and model configuration settings
- `framingham.csv`: Framingham Heart Study dataset
- `requirements.txt`: Required Python packages
- `templates/`: HTML templates for the web application
  - `index.html`: Home page
  - `predict.html`: Risk assessment form
  - `result.html`: Prediction results display
  - `about.html`: Information about the Framingham model
  - `health_tips.html`: Cardiovascular health recommendations
- `static/`: CSS, JavaScript, and image files

## Model Features

The Framingham Heart Disease model uses the following features:
- **Demographics**: Age, Gender, Education level
- **Lifestyle**: Smoking status, Cigarettes per day
- **Medical History**: Blood pressure medication, Previous stroke, Hypertension, Diabetes
- **Measurements**: Total cholesterol, Systolic blood pressure, Diastolic blood pressure, BMI, Heart rate, Glucose levels

## License

This project is licensed under the MIT License - see the LICENSE file for details.
<<<<<<< HEAD

## Acknowledgments

- Based on the Framingham Heart Study dataset
- Implementation using Random Forest classification model

