#AI Model For Diet Recommendation

import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv("data/diet_data.csv")
    X = data[["age", "weight"]]
    y = data["recommended_diet"]
    model = LogisticRegression()
    model.fit(X, y)
    return model