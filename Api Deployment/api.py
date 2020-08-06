import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("/Users/satyamkumar/Desktop/machinelearning/codecops-hackathon/Api Deployment/model.pkl",'rb')

df = pd.DataFrame()
@app.route('/')
def home():
    return render_template('/Users/satyamkumar/Desktop/machinelearning/codecops-hackathon/Api Deployment/Templates/form.html')
@app.route('/predict',methods=['POST'])
def predict():
    global df
    input_features = [x for x in request.form.values()]
    Name = input_features[0]
    Phone = input_features[1]
    Budget = input_features[2]
    Years = input_features[3]
    Interest= input_features[4]
    Amount_of_down_paymnet = input_features[5]
    predicted_price = model.dtr.predict(new)
    return render_template('/Users/satyamkumar/Desktop/machinelearning/codecops-hackathon/Api Deployment/Templates/form.html',prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))


if __name__ == "__main__":
    app.run()