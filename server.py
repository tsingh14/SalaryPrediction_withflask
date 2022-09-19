# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:43:34 2022

@author: singh
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict1():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    
    output = prediction[0]
    return jsonify(output)

@app.route('/apilist',methods=['POST'])
def predict2():
    data = request.get_json(force=True)
    output=[]
    for i in data['exp']:
        #print()
        prediction = model.predict([[np.array(i)]])
        output.append(prediction[0])
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
