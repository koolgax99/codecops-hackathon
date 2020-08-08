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
    total = b - ((b*rate*12)/100)

    final_features = [[np.array(total)]]
    prediction = model.predict(final_features)

    area = round(prediction[0][0],2)
    bhk = round(prediction[0][1],2)
    bathroom = round(prediction[0][2],2)
    parking = round(prediction[0][4],2)
    
    if(round(prediction[0][3],2)==1):
        furnishing="Un-furnished"
    elif (round(prediction[0][3],2)==2):
        furnishing="Semi-Furnished"
    else:
        furnishing="Fully-Furnished"

    if(round(prediction[0][5],2)==1):
        status="Ready To Move"
    else:
        status="Almost Ready"

    if(round(prediction[0][6],2)==1):
        transaction="New Property"
    else:
        transaction="Resale"
    
    if(round(prediction[0][7],2)==1):
        typehouse="Builder Floor"
    else:
        typehouse="Apartment"

    return render_template('index.html',principal='{}'.format(principal),total='{}'.format(total), area='Area = {}'.format(area) , bhk='BHK= {}'.format(bhk), bathroom='Bathroom = {}'.format(bathroom),  furnishing='Furnishing Status= {}'.format(furnishing), parking='Parking = {}'.format(parking),  status='House Status = {}'.format(status), transaction='Transaction of House = {}'.format(transaction),  typehouse='Type of House = {}'.format(typehouse))


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