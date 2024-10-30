# streamlit_app.py

# Section 1: Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import joblib  # New import for loading the model
from solubility_simulation import calculate_degree_of_ionization, dissolution_profile, find_optimal_solubility

# Load the pre-trained model
model = joblib.load('solubility_predictor_model.pkl')

# Section 2: Title and Introduction
st.title("Drug Solubility Simulation and AI Prediction in GI Environments")

# Section 3: Dynamic Drug Properties
st.subheader("Drug Properties")
pKa = st.number_input("Enter pKa of the drug", min_value=0.0, max_value=14.0, value=8.1)  # Default to Azithromycin
concentration = st.slider("Tablet Concentration (mg)", 100, 1000, 500)
molecular_weight = st.number_input("Enter molecular weight (optional, for future features)", min_value=0.0, value=748.0)
dissolution_rate = st.slider("Dissolution Rate Constant", 0.01, 0.2, 0.1)

# Section 4: Environment pH Controls
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

# Section 5: Calculations and Results
time_steps, solubility_profile = dissolution_profile(pKa, concentration, environment_data, dissolution_rate)
optimal_env, max_solubility = find_optimal_solubility(solubility_profile)

st.write(f"Optimal Environment: {optimal_env}")
st.write(f"Max Solubility: {max_solubility:.2f} mg")

# AI-Predicted Solubility
st.subheader("AI-Predicted Solubility")
predicted_solubility = []
for env in environment_data:
    pH = env['pH']
    features = np.array([[pKa, pH, dissolution_rate]])
    predicted_value = model.predict(features)[0]
    predicted_solubility.append(predicted_value)

# Section 6: Plotting - Simulated vs. Predicted
fig, ax = plt.subplots()
for i, (env, solubility) in enumerate(solubility_profile.items()):
    env_pH = environment_data[i]['pH']
    ax.plot(time_steps, solubility, label=f"{env} (Simulated, pH {env_pH})")

# Plot predicted solubility as a horizontal line
for i, env in enumerate(environment_data):
    ax.hlines(predicted_solubility[i], xmin=time_steps[0], xmax=time_steps[-1],
              linestyles='dashed', label=f"{env['name']} (Predicted)")
    
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Dissolved Amount (mg)")
ax.legend(title="GI Regions and Solubility")

st.pyplot(fig)
