# 🫀 Cardio Guide - Heart Disease Risk Predictor

<div align="center">
  <img src="static/images/logo.png" alt="Cardio Guide Logo" width="250">
  <p><i>AI-powered heart disease risk prediction based on the Framingham Heart Study</i></p>
  
  ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
  ![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
  ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-red.svg)
  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
</div>

## 📋 Overview

Cardio Guide is an interactive web application that uses machine learning to predict an individual's 10-year risk of developing coronary heart disease. Built with the validated Framingham Heart Study model, it provides personalized risk assessment and evidence-based recommendations for heart health management.

![Dashboard Screenshot](static/images/screenshots/dashboard.png)
*The Cardio Guide homepage with risk assessment options*

## ✨ Key Features

### 🔍 Personalized Heart Risk Assessment
Analyze your risk factors using the scientifically validated Framingham Heart Study model to receive a personalized 10-year coronary heart disease risk prediction.

![Assessment Form](static/images/screenshots/assessment_form.png)
*The multi-step assessment form collects relevant health information*

### 📊 Interactive Results Dashboard
Receive a comprehensive breakdown of your risk factors with detailed visualizations showing how each parameter contributes to your overall heart disease risk.

![Results Dashboard](static/images/screenshots/results_dashboard.png)
*Detailed risk assessment results with visual indicators*

### 💬 AI-Powered Health Assistant
Get answers to your heart health questions through our AI health assistant that provides evidence-based information on heart disease, risk factors, and lifestyle modifications.

![Health Assistant](static/images/screenshots/health_assistant.png)
*The AI-powered health assistant answering questions about heart health*

### 💡 Personalized Health Tips
Access tailored recommendations for improving cardiovascular health based on scientific research and clinical guidelines.

![Health Tips](static/images/screenshots/health_tips.png)
*Curated heart health tips and lifestyle recommendations*

### ℹ️ Educational Resources
Learn about the Framingham Heart Study, risk factors, and how the predictive model works through our educational resources.

![About the Model](static/images/screenshots/about_model.png)
*Information about the Framingham model and its performance metrics*

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cardio-guide.git
   cd cardio-guide
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## 🧠 Technical Architecture

![Technical Architecture](static/images/screenshots/architecture.png)
*The application's technical architecture diagram*

### Components
- **Frontend**: HTML5, CSS3, JavaScript, Chart.js for visualizations
- **Backend**: Flask (Python) with REST API endpoints
- **ML Model**: Random Forest Classifier trained on Framingham Heart Study dataset
- **Data Processing**: Pandas for data manipulation and preprocessing
- **Health Assistant**: Pattern matching and knowledge-based AI chatbot

## 📁 Project Structure

```
cardio-guide/
├── app.py                  # Main Flask application
├── model.py                # Framingham model implementation
├── chatbot_responses.py    # Health assistant response patterns
├── config.py               # Configuration settings
├── model1.pk1              # Pre-trained heart disease model
├── framingham.csv          # Dataset for training/reference
├── requirements.txt        # Python dependencies
├── static/                 # Static assets
│   ├── css/                # CSS stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images and icons
└── templates/              # HTML templates
    ├── index.html          # Homepage
    ├── predict.html        # Assessment form
    ├── result.html         # Results display
    ├── about.html          # About the model
    ├── health_tips.html    # Health recommendations
    └── chatbot.html        # Health assistant interface
```

## 📊 Model Details

The Framingham Heart Disease prediction model uses the following features:

| Category | Features |
|----------|----------|
| **Demographics** | Age, Gender, Education level |
| **Lifestyle** | Smoking status, Cigarettes per day |
| **Medical History** | BP medication, Previous stroke, Hypertension, Diabetes |
| **Measurements** | Total cholesterol, Systolic BP, Diastolic BP, BMI, Heart rate, Glucose |

## 📝 Model Performance

The model achieves the following performance metrics on the test dataset:

- **Accuracy**: 85.2%
- **Precision**: 73.1%
- **Recall**: 67.8%
- **F1 Score**: 70.3%
- **AUC-ROC**: 0.829

![Model Performance](static/images/screenshots/model_metrics.png)
*Visualization of the model's performance metrics*

## 📱 Responsive Design

The application is fully responsive and works seamlessly across desktop, tablet, and mobile devices.

<div align="center">
  <img src="static/images/screenshots/mobile_view.png" alt="Mobile View" width="200">
  <p><i>Cardio Guide on mobile devices</i></p>
</div>

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact


Anuranjan Jain - [@jainanuranjan](https://twitter.com/jainanuranjan) 

Project Link: [https://github.com/anuranjanjain/DSN2](https://github.com/anuranjanjain/DSN2)



<div align="center">
  <p>Made with ❤️ for heart health</p>
</div>
