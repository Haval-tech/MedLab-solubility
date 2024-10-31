# streamlit_app.py
import streamlit as st
from solubility_simulation import get_drug_data, calculate_ionization, get_pH_ranges
from plot_settings import plot_solubility
from layout_settings import setup_layout

# Set up the layout
setup_layout()

# Title
st.title("MedLab Drug Solubility Simulation Tool")

# Choose input mode
input_mode = st.radio("Choose input mode:", ["API Search", "Manual Input"])

# Get pKa based on input mode
pKa = None
if input_mode == "API Search":
    drug_name = st.text_input("Enter drug name to search for pKa:")
    if drug_name:
        pKa = get_drug_data(drug_name)
        if pKa:
            st.write(f"Found pKa for {drug_name}: {pKa}")
        else:
            st.write("pKa information not available. Use manual input for custom values.")
else:
    pKa = st.number_input("Enter known pKa value:", min_value=0.0, max_value=14.0, step=0.1)

# Environment selection
st.sidebar.header("Choose Environment")
environments = {
    "Stomach": (1, 3),
    "Duodenum": (5, 6),
    "Jejunum": (6, 7),
    "Ileum": (7, 8)
}
selected_env = [env for env in environments.keys() if st.sidebar.checkbox(env)]

# Calculate and plot if pKa and environments are provided
if pKa is not None and selected_env:
    pH_ranges = get_pH_ranges(selected_env, environments)
    ionized_percentages = [calculate_ionization(pKa, pH) for pH in pH_ranges]
    plot_solubility(ionized_percentages)
