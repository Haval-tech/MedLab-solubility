# plot_settings.py

import matplotlib.pyplot as plt
import streamlit as st

def plot_simulated_profile(time_steps, solubility_profile, selected_environments):
    fig, ax = plt.subplots()
    for env in selected_environments:
        env_name = env['name']
        ax.plot(time_steps, solubility_profile[env_name], label=f"{env_name} (Simulated, pH {env['pH']})")
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Dissolved Amount (mg)")
    ax.legend(title="Simulated GI Regions and Solubility")
    st.pyplot(fig)

def plot_ai_predictions(time_steps, selected_environments, model, pKa, dissolution_rate):
    fig, ax = plt.subplots()
    for env in selected_environments:
        env_name = env['name']
        predicted_solubility = []
        for t in time_steps:
            features = np.array([[pKa, env['pH'], dissolution_rate, t]])
            predicted_value = model.predict(features)[0]
            predicted_solubility.append(predicted_value)
        ax.plot(time_steps, predicted_solubility, label=f"{env_name} (Predicted, pH {env['pH']})", linestyle="--")
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Dissolved Amount (mg)")
    ax.legend(title="Predicted GI Regions and Solubility")
    st.pyplot(fig)
