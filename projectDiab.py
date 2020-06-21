import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle
from joblib import load

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
    output=prediction[0]
    if(ouput==0):
        pred="Paitent doesnt have diabetes"
    else:
        pred="Paitent has diabetes"
    return render_template('NewDiabetes.html',prediction_text='Diabetes Milletus Prediction {}'.format(pred))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data=request.get_json(force=True)
    prediction=model.y_predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)


if __name__== "__main__":

    app.run(debug=True)
    