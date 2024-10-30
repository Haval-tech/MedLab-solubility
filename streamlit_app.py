# streamlit_app.py

# Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import joblib
from solubility_simulation import calculate_degree_of_ionization, dissolution_profile, find_optimal_solubility

# Check if model file exists, if not, train and save it
model_path = 'solubility_predictor_model.pkl'
if not os.path.exists(model_path):
    # Train a simple regression model as a placeholder
    np.random.seed(42)
    X = np.random.rand(100, 3) * [14, 10, 0.2]  # Mock data [pKa, pH, dissolution rate]
    y = X[:, 0] * 10 + X[:, 1] * 5 + X[:, 2] * 100  # Mock solubility function

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, model_path)
else:
    # Load the pre-trained model
    model = joblib.load(model_path)

# Title
st.title("Drug Solubility Simulation and AI Prediction in GI Environments")

# Drug Properties
st.subheader("Drug Properties")
pKa = st.number_input("Enter pKa of the drug", min_value=0.0, max_value=14.0, value=8.1)  # Default to Azithromycin
concentration = st.slider("Tablet Concentration (mg)", 100, 1000, 500)
molecular_weight = st.number_input("Enter molecular weight (optional, for future features)", min_value=0.0, value=748.0)
dissolution_rate = st.slider("Dissolution Rate Constant", 0.01, 0.2, 0.1)

# Environment pH Controls
st.subheader("GI Environment pH Levels")
stomach_pH = st.slider("Stomach pH", min_value=1.0, max_value=3.0, value=2.0)
duodenum_pH = st.slider("Duodenum pH", min_value=3.0, max_value=7.0, value=5.0)
jejunum_pH = st.slider("Jejunum pH", min_value=5.5, max_value=7.5, value=6.5)
ileum_pH = st.slider("Ileum pH", min_value=6.5, max_value=8.0, value=7.5)

environment_data = [
    {'name': 'Stomach', 'pH': stomach_pH},
    {'name': 'Duodenum', 'pH': duodenum_pH},
    {'name': 'Jejunum', 'pH': jejunum_pH},
    {'name': 'Ileum', 'pH': ileum_pH}
]

# Calculate and Display Solubility Profile
time_steps, solubility_profile = dissolution_profile(pKa, concentration, environment_data, dissolution_rate)
optimal_env, max_solubility = find_optimal_solubility(solubility_profile)

st.write(f"Optimal Environment: {optimal_env}")
st.write(f"Max Solubility: {max_solubility:.2f} mg")

# AI-Predicted Solubility Over Time
st.subheader("AI-Predicted Solubility Over Time")
predicted_solubility_profile = {}

for env in environment_data:
    pH = env['pH']
    env_name = env['name']
    predicted_solubility = []

    # Predict solubility at each time step
    for t in time_steps:
        features = np.array([[pKa, pH, dissolution_rate * t]])
        predicted_value = model.predict(features)[0]
        predicted_solubility.append(predicted_value)

    # Store the predictions for each environment
    predicted_solubility_profile[env_name] = predicted_solubility

# Plotting - Simulated vs. Predicted Over Time
fig, ax = plt.subplots()
for i, (env, solubility) in enumerate(solubility_profile.items()):
    env_pH = environment_data[i]['pH']
    ax.plot(time_steps, solubility, label=f"{env} (Simulated, pH {env_pH})", linestyle='-')

# Plot predicted solubility as a time-varying line
for env, predicted_solubility in predicted_solubility_profile.items():
    ax.plot(time_steps, predicted_solubility, label=f"{env} (Predicted)", linestyle='--')

ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Dissolved Amount (mg)")
ax.legend(title="GI Regions and Solubility")

st.pyplot(fig)
