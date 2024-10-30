import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Generate mock data for training (replace this with real data if available)
# Variables: [pKa, pH, dissolution_rate]
# Target: solubility
np.random.seed(42)
X = np.random.rand(100, 3) * [14, 10, 0.2]  # [pKa, pH, dissolution rate]
y = X[:, 0] * 10 + X[:, 1] * 5 + X[:, 2] * 100  # Mock solubility function

# Train a simple regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'solubility_predictor_model.pkl')
print("Model trained and saved!")
