# streamlit_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from layout_settings import setup_layout

# Set up layout
setup_layout()

# Title
st.title("Drug Solubility Simulation Tool")

# Instructions
st.write("### Input Parameters")
st.write("This tool simulates drug solubility over time in different gastrointestinal environments.")

# Input fields
pKa = st.number_input("Enter the pKa of the drug:", min_value=0.0, max_value=14.0, step=0.1)
concentration_mg = st.number_input("Enter drug concentration (mg):", min_value=0.0, step=0.1)

# Environment selection
st.write("### Select the Environment(s)")
environments = {
    "Stomach": (1, 3),
    "Duodenum": (5, 6),
    "Jejunum": (6, 7),
    "Ileum": (7, 8)
}
selected_env = [env for env in environments.keys() if st.checkbox(env)]

# Calculation and Output
if pKa and concentration_mg and selected_env:
    st.write("### Simulation Results")

    # Convert concentration from mg to molarity (assuming 1 L for simplicity)
    concentration_molar = concentration_mg / 1000  # Simple conversion for demonstration

    # Function to calculate ionization percentage
    def calculate_ionization(pKa, pH):
        ratio = 10 ** (pH - pKa)
        ionized = ratio / (1 + ratio) * 100
        return ionized

    # Create plot data
    fig, ax = plt.subplots(figsize=(12, 6))
    time_range = np.linspace(0, 120, 100)  # Simulate time from 0 to 120 minutes

    report_data = []

    for env in selected_env:
        pH_min, pH_max = environments[env]
        pH_range = np.linspace(pH_min, pH_max, 50)  # Range of pH values for each environment
        ionized_percentages = [calculate_ionization(pKa, pH) for pH in pH_range]
        
        # Create a gradual increase in solubility over time for a curvy effect
        solubility_over_time = np.array([np.mean(ionized_percentages) * concentration_molar * (1 - np.exp(-t/40)) for t in time_range])

        # Plot the solubility curve
        ax.plot(time_range, solubility_over_time, label=f"{env} (pH {pH_min}-{pH_max})", linewidth=2)

        # Store data for the report
        avg_solubility = solubility_over_time[-1]  # Solubility at the end of 120 minutes
        time_to_50_solubility = time_range[np.argmax(solubility_over_time >= 0.5 * avg_solubility)]
        report_data.append((env, pH_min, pH_max, avg_solubility, time_to_50_solubility))

    # Finalize plot
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Solubility (%)")
    ax.set_ylim(0, max(solubility_over_time) * 2)  # Zoom out by setting a broad y-limit
    ax.set_title("Solubility Over Time in Selected Environments")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

    # Display report below the graph
    st.write("### Report")
    for env, pH_min, pH_max, avg_solubility, time_to_50_solubility in report_data:
        st.write(f"**{env}** (pH {pH_min}-{pH_max}): Final Solubility = {avg_solubility:.2f}% of concentration ({concentration_molar:.2f} M) at 120 minutes")
        st.write(f"Time to reach 50% of final solubility: {time_to_50_solubility:.1f} minutes")
