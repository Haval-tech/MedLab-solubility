# plot_settings.py
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_solubility(ionized_percentages=None, labels=None):
    # Handle cases where no data is provided
    if ionized_percentages is None or not ionized_percentages or not ionized_percentages[0]:
        ionized_percentages = [[0]]  # Default empty data for initial plot
        labels = ["No Data"]

    # Generate time range for x-axis based on the length of ionized_percentages data
    time_range = np.linspace(0, len(ionized_percentages[0]), len(ionized_percentages[0]))

    # Plot the graph with a smaller figure size
    fig, ax = plt.subplots(figsize=(8, 4))  # Adjust size to zoom out a bit

    # Plot each environment's data separately with distinct labels
    for i, data in enumerate(ionized_percentages):
        ax.plot(time_range, data, label=labels[i])

    ax.set_xlabel('Time')
    ax.set_ylabel('Solubility Percentage')
    ax.set_title("Solubility Percentage over Time")
    ax.legend()
    st.pyplot(fig)
