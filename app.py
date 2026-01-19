import pickle
from flask import Flask, request,app, json, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
rgmodel = pickle.load(open('regression_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    x = np.array(data['x'])
    y = rgmodel.predict(x)
    return json.dumps({'y': y.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
 