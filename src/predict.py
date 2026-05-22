# src/predict.py
''' 
# old working file
import joblib
import numpy as np


model = joblib.load('models/best_rf_fraud_model.joblib')
scaler = joblib.load('models/fraud_scaler.joblib')


def predict_transaction(input_data):
    input_array = np.asarray(input_data)
    reshaped_input = input_array.reshape(1, -1)

    scaled_input = scaler.transform(reshaped_input)

    prediction = model.predict(scaled_input)

    if prediction[0] == 0:
        return "Normal Transaction"
    else:
        return "Fraudulent Transaction"

'''

import numpy as np


def predict_transaction(model, input_data):

    input_array = np.array(input_data).reshape(1, -1)

    probability = model.predict_proba(input_array)[0][1]

    # Custom fraud threshold

    prediction = 1 if probability > 0.30 else 0

    return prediction, probability