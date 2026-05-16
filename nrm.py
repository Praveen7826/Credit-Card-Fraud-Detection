import pandas as pd

data = pd.read_csv("data/creditcard.csv")

print(data[data['Class'] == 1].head(1))