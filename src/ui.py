import streamlit as st


def custom_ui():

    st.markdown("""
    
    <style>

    .stApp {
        background: linear-gradient(to right, #0f172a, #111827);
        color: white;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #00E5FF;
        text-align: center;
    }

    .subtitle {
        font-size: 18px;
        color: #CBD5E1;
        text-align: center;
    }

    div[data-testid="metric-container"] {
        background-color: #1E293B;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 15px;
    }

    </style>

    """, unsafe_allow_html=True)