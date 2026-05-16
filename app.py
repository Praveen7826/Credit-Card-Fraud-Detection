# app.py

import streamlit as st
import numpy as np
from src.predict import predict_transaction


st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered"
)


st.title("💳 Credit Card Fraud Detection System")
st.write("Enter transaction details below to predict fraud.")


input_data = []

for i in range(30):
    value = st.number_input(f"Feature {i + 1}", value=0.0)
    input_data.append(value)


if st.button("Predict Transaction"):
    result = predict_transaction(input_data)

    if result == "Fraudulent Transaction":
        st.error(f"Prediction: {result}")
    else:
        st.success(f"Prediction: {result}")
