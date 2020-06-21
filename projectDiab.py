import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle

app=Flask(__name__)
model= pickle.load(open('decision.pkl','rb'))

@app.route('/')
def home():
    return render_template('NewDiabetes.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
   '''
    x_test=[[int(x) for x in request.form.values()]]
    print(x_test)
    sc=load('scaler.save')
    prediction =model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[0][0]
    return render_template('NweDiabetes.html',prediction_text='Diabetes Milletus Prediction {}'.format(pred))

if __name__== "__main__":
    app.run(debug=True)
    