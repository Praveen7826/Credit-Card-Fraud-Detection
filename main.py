# main.py

from src.preprocessing import load_data, preprocess_data
from src.train_model import train_model, evaluate_model
from src.utils import create_directories


create_directories()


data = load_data('data/creditcard.csv')

X_train, X_test, y_train, y_test = preprocess_data(data)

model = train_model(X_train, y_train)

print("\nModel Training Completed Successfully!\n")

evaluate_model(model, X_test, y_test)