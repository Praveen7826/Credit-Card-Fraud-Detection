import streamlit as st
import joblib

@st.cache_resource
def load_model():

    model = joblib.load("models/best_rf_fraud_model.joblib")

    return model