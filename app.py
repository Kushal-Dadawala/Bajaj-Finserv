from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def home():
    return "Lab Reports Analysis API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Add your prediction logic here
        return jsonify({"status": "success", "prediction": "Sample prediction"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
