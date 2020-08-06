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
    int_features = [int(x) for x in request.form.values()]

    a = (int_features[0]*int_features[1]*12) 
    b = a + int_features[2]
    c = b - ((b*int_features[3]*12)/100)

    final_features = [[np.asarray(c)]]
    prediction = model.predict(final_features)

    output = round(prediction[0][0],2)
    output1 = round(prediction[0][1],2)
    """
print("Expected Bathroom :  ",pred[0][2])
print("Expected Furnishing :  ",pred[0][3])
print("Expected Parking :  ",pred[0][4])
print("Expected Status :  ",pred[0][5])
print("Expected Transaction :  ",pred[0][5])
print("Expected Type :  ",pred[0][6])
""" 

    return render_template('index.html', prediction_text='test status= {} bathroom= {} '.format(output, output1) )

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