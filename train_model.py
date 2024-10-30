# train_model.py

import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

def load_trained_model():
    model_path = 'solubility_predictor_model.pkl'
    if not os.path.exists(model_path):
        # Code for training the model (as previously provided)
        np.random.seed(42)
        X = np.random.rand(100, 4)  # Mock data [pKa, pH, dissolution rate, time]
        y = X[:, 0] * 10 + X[:, 1] * 5 + X[:, 2] * 50 + X[:, 3] * 0.5  # Mock target
        model = LinearRegression()
        model.fit(X, y)
        joblib.dump(model, model_path)
    else:
        model = joblib.load(model_path)
    return model
