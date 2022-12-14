from flask import Flask, render_template, request, url_for, redirect
import joblib
import pandas as pd
import numpy as np
import sklearn
import gunicorn
import xgboost


# load our model file
model = joblib.load('model.gbr')
scale = joblib.load('scaler.sc')

# Object for Flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # GET ALL DATA AND SCALIZED

        age = request.form['age']

        sex = int(request.form['sex'])

        bmi = request.form['bmi']

        children = request.form['children']

        smoker = int(request.form['smoker'])


        # 2. create DataFrame
        data = [[age, sex, bmi, children, smoker]]
        column_name = ['age', 'sex', 'bmi', 'children', 'smoker']

        data_model = pd.DataFrame(data, columns=column_name)

        # scalized
        num_col = ['age', 'bmi', 'children']
        data_model[num_col] = scale.transform(data_model[num_col])

        # Prediction
        result = model.predict(data_model)[0]

        result= round(float(result), 2)

        # 3. Display

        return render_template('index.html', Predict_Text=f'Predict Premium is {result}')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
