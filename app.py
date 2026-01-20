import pickle
from flask import Flask, request,app, json, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
rgmodel = pickle.load(open('regression_model.pkl', 'rb'))

@app.route ('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)