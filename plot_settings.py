# plot_settings.py
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_solubility(ionized_percentages):
    time_range = np.linspace(0, len(ionized_percentages), len(ionized_percentages))
    fig, ax = plt.subplots()
    ax.plot(time_range, ionized_percentages, label='Solubility (%)', color='blue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Solubility Percentage')
    ax.set_title("Solubility Percentage over Time")
    st.pyplot(fig)
