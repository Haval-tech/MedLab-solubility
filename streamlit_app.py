import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate ionization
def calculate_ionization(pKa, pH):
    ratio = 10 ** (pH - pKa)
    ionized = ratio / (1 + ratio) * 100
    non_ionized = 100 - ionized
    return ionized, non_ionized

# Streamlit UI
st.title("Drug Solubility Simulation Tool")

# User input for pKa
pKa = st.number_input("Enter the pKa value of the substance:", min_value=0.0, max_value=14.0, step=0.01)

# Set pH range
pH_range = np.linspace(1, 10, 100)  # default pH range from 1 to 10

# Only proceed if pKa is entered
if pKa:
    # Calculate ionization over the pH range
    ionized_percentages = []
    non_ionized_percentages = []

    for pH in pH_range:
        ionized, non_ionized = calculate_ionization(pKa, pH)
        ionized_percentages.append(ionized)
        non_ionized_percentages.append(non_ionized)

    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(pH_range, ionized_percentages, label='Ionized (%)', color='blue')
    ax.plot(pH_range, non_ionized_percentages, label='Non-Ionized (%)', color='red')
    ax.set_xlabel('pH')
    ax.set_ylabel('Percentage')
    ax.set_title(f'Degree of Ionization vs. pH (pKa = {pKa})')
    ax.legend()
    st.pyplot(fig)
