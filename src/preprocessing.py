# src/preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    X = data.drop('Class', axis=1)
    y = data['Class']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, 'models/fraud_scaler.joblib')

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled,
        y_resampled,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test
