from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained AI model
with open('model1.pk1', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html')

@app.route('/health_tips')
def health_tips():
    return render_template('health_tips.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input and convert to numpy array
        data = [float(request.form[key]) for key in request.form]
        data = np.array(data).reshape(1, -1)  # Reshape for model input

        # Make prediction
        prediction = model.predict_proba(data)[0][1] * 100  # Probability of disease

        # Redirect to the results page with the prediction
        return redirect(url_for('result', prediction=round(prediction, 2)))
    except Exception as e:
        return render_template('result.html', error=str(e))

@app.route('/result')
def result():
    prediction = request.args.get('prediction', None)
    error = request.args.get('error', None)

    return render_template('result.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
