import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load(open(r'model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template(r'index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    budget = int(request.form['budget'])
    years = int(request.form['years'])
    rate = int(request.form['rate'])
    principal = int(request.form['principal'])

    a = (budget*years*12)
    b = a + principal
    c = b - ((b*rate*12)/100)

    final_features = [[np.array(c)]]
    prediction = model.predict(final_features)

    area = round(prediction[0][0],2)
    bhk = round(prediction[0][1],2)
    bathroom = round(prediction[0][2],2)
    furnishing= round(prediction[0][3],2)
    parking = round(prediction[0][4],2)
    status = round(prediction[0][5],2)
    transaction = round(prediction[0][6],2)
    typehouse = round(prediction[0][7],2)

    return render_template('index.html', area='area = {}'.format(area) , bhk='bhk= {}'.format(bhk), bathroom='bathroom = {}'.format(bathroom),  furnishing='furnishing = {}'.format(furnishing), parking='parking = {}'.format(parking),  status='status = {}'.format(status), transaction='transaction = {}'.format(transaction),  typehouse='typehouse = {}'.format(typehouse))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0][5]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)