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
