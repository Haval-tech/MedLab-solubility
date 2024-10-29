# streamlit_app.py

import streamlit as st
import matplotlib.pyplot as plt
from solubility_simulation import calculate_degree_of_ionization, dissolution_profile, find_optimal_solubility

st.title("Azithromycin 500mg Solubility Simulation")

# Input parameters
pKa = 8.1
concentration = st.slider("Tablet Concentration (mg)", 100, 1000, 500)
dissolution_rate = st.slider("Dissolution Rate Constant", 0.01, 0.2, 0.1)

# Environment data for various body regions
environment_data = [
    {'name': 'stomach', 'pH': 2.0},
    {'name': 'duodenum', 'pH': 5.0},
    {'name': 'jejunum', 'pH': 6.5},
    {'name': 'ileum', 'pH': 7.5}
]

# Run simulation
time_steps, solubility_profile = dissolution_profile(pKa, concentration, environment_data, dissolution_rate)
optimal_env, max_solubility = find_optimal_solubility(solubility_profile)

# Display results
st.write(f"Optimal Environment: {optimal_env}")
st.write(f"Max Solubility: {max_solubility:.2f} mg")

# Plotting
fig, ax = plt.subplots()
for env, solubility in solubility_profile.items():
    ax.plot(time_steps, solubility, label=f"{env} (pH {environment_data[0]['pH']})")
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Dissolved Amount (mg)")
ax.legend()
st.pyplot(fig)
