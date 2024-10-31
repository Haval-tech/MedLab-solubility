# plot_settings.py
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_solubility(ionized_percentages=None, labels=None):
    # If no data provided, set up empty data
    if ionized_percentages is None:
        ionized_percentages = []
    if labels is None:
        labels = ["No Data"]

    # Generate time range for x-axis (assuming it's the same length as ionized_percentages)
    time_range = np.linspace(0, len(ionized_percentages[0]) if ionized_percentages else 1, len(ionized_percentages[0]) if ionized_percentages else 1)

    # Plot the graph with a smaller figure size
    fig, ax = plt.subplots(figsize=(8, 4))  # Adjust size to zoom out a bit

    # Plot each environment's data separately
    for i, data in enumerate(ionized_percentages):
        ax.plot(time_range, data, label=labels[i])

    ax.set_xlabel('Time')
    ax.set_ylabel('Solubility Percentage')
    ax.set_title("Solubility Percentage over Time")
    ax.legend()
    st.pyplot(fig)
