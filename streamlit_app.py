# streamlit_app.py

# Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import joblib
from solubility_simulation import calculate_degree_of_ionization, dissolution_profile, find_optimal_solubility

# Load or train model
model_path = 'solubility_predictor_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please ensure solubility_predictor_model.pkl is in the app directory.")

# Sidebar for Inputs
st.sidebar.title("Acid-Base Simulation Controls")
st.sidebar.subheader("Drug Properties")
pKa = st.sidebar.slider("pKa", min_value=0.0, max_value=14.0, value=8.1)
concentration = st.sidebar.slider("Concentration (mg)", 100, 1000, 500)
dissolution_rate = st.sidebar.slider("Dissolution Rate", 0.01, 0.2, 0.1)

# Environment pH Controls
st.sidebar.subheader("Select Environment")
selected_environments = []
if st.sidebar.checkbox("Stomach"):
    selected_environments.append({'name': 'Stomach', 'pH': st.sidebar.slider("Stomach pH", 1.0, 3.0, 2.0)})
if st.sidebar.checkbox("Duodenum"):
    selected_environments.append({'name': 'Duodenum', 'pH': st.sidebar.slider("Duodenum pH", 3.0, 7.0, 5.0)})
if st.sidebar.checkbox("Jejunum"):
    selected_environments.append({'name': 'Jejunum', 'pH': st.sidebar.slider("Jejunum pH", 5.5, 7.5, 6.5)})
if st.sidebar.checkbox("Ileum"):
    selected_environments.append({'name': 'Ileum', 'pH': st.sidebar.slider("Ileum pH", 6.5, 8.0, 7.5)})

# Ensure we have at least one environment selected
if not selected_environments:
    st.warning("Please select at least one environment to simulate.")
elif 'model' not in locals():
    st.warning("AI model is not available. Ensure the model file is loaded.")
else:
    # Calculate and Display Simulated Solubility Profile
    time_steps, solubility_profile = dissolution_profile(pKa, concentration, selected_environments, dissolution_rate)

    # Simulated Solubility Profile
    st.subheader("Simulated Solubility Profile")
    fig1, ax1 = plt.subplots()
    for env in selected_environments:
        env_name = env['name']
        ax1.plot(time_steps, solubility_profile[env_name], label=f"{env_name} (Simulated, pH {env['pH']})")
    ax1.set_xlabel("Time (minutes)")
    ax1.set_ylabel("Dissolved Amount (mg)")
    ax1.legend(title="Simulated GI Regions and Solubility")
    st.pyplot(fig1)

    # AI-Predicted Solubility Profile
    st.subheader("AI-Predicted Solubility Profile")
    fig2, ax2 = plt.subplots()
    for env in selected_environments:
        env_name = env['name']
        predicted_solubility = []

        # Generate predictions over time
        for t in time_steps:
            features = np.array([[pKa, env['pH'], dissolution_rate, t]])
            predicted_value = model.predict(features)[0]
            predicted_solubility.append(predicted_value)

        ax2.plot(time_steps, predicted_solubility, label=f"{env_name} (Predicted, pH {env['pH']})")
    ax2.set_xlabel("Time (minutes)")
    ax2.set_ylabel("Dissolved Amount (mg)")
    ax2.legend(title="Predicted GI Regions and Solubility")
    st.pyplot(fig2)
