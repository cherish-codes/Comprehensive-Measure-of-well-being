from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained Linear Regression model you just generated!
with open('HDI.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    # Renders your introductory homepage user interface
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Capture the data inputs entered by the user in the web forms
            life_exp = float(request.form['life_exp'])
            exp_school = float(request.form['exp_school'])
            mean_school = float(request.form['mean_school'])
            gni = float(request.form['gni'])
            
            # Country placeholder value (matches our encoded feature size)
            country_encoded = 0.0 
            
            # Format inputs into an array for model testing/evaluation
            features = np.array([[country_encoded, life_exp, exp_school, mean_school, gni]])
            
            # Run prediction logic
            prediction = model.predict(features)[0]
            
            # Restrict HDI bounds logically between 0.0000 and 1.0000
            prediction = max(0.0, min(1.0, prediction))
            
            return render_template('index.html', 
                                   prediction_text=f'Predicted Human Development Index (HDI): {prediction:.4f}')
        except Exception as e:
            return render_template('index.html', prediction_text="Error processing values. Please check your numbers.")

if __name__ == "__main__":
    app.run(debug=True)