import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
import pickle
app = Flask(__name__)
model = pickle.load(open(r'C:\Users\91915\Downloads\Telegram Desktop\flask\flask\rrc_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():

    a = request.form['z']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    e = request.form['e']
    f = request.form['f']
    g = request.form['g']
    h = request.form['h']
    i = request.form['i']
    j = request.form['j']
    k = request.form['k']
    

    total = [[a,b,c,d,e,f,g,h,i,j,k]]
    prediction = model.predict(total)

    if(prediction==0):
        output = "Bad"
    else:
        output="Good"
    
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=False)#running our app
            