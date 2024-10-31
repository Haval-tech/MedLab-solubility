import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt

# Function to fetch drug data from PubChem API
def get_drug_data(drug_name):
    # Search PubChem by drug name
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/IUPACName,pKa/JSON"
    response = requests.get(search_url)
    if response.status_code


# Streamlit app UI
st.title("Drug Solubility Simulation Tool")

# Option to select input mode: API or Manual
input_mode = st.radio("Choose input mode:", ["API Search", "Manual Input"])

# Option 1: API Search
if input_mode == "API Search":
    drug_name = st.text_input("Enter drug name to search for pKa:")

    if drug_name:
        pKa = get_drug_data(drug_name)
        if pKa:
            st.write(f"Found pKa for {drug_name}: {pKa}")
        else:
            st.write("pKa information not available for this drug. Switch to manual input for custom values.")
else:
    # Option 2: Manual Input
    pKa = st.number_input("Enter known pKa value:", min_value=0.0, max_value=14.0, step=0.1)

# Common inputs for both modes
if pKa:
    # Select environment
    environment = st.selectbox("Choose environment:", ["Stomach (pH 1-3)", "Intestine (pH 5-8)", "Custom"])
    
    # Set pH range based on environment
    if environment == "Stomach (pH 1-3)":
        pH_range = np.linspace(1, 3, 100)
    elif environment == "Intestine (pH 5-8)":
        pH_range = np.linspace(5, 8, 100)
    else:
        # Custom pH range input
        pH_min = st.number_input("Enter minimum pH:", min_value=0.0, max_value=14.0, value=1.0, step=0.1)
        pH_max = st.number_input("Enter maximum pH:", min_value=0.0, max_value=14.0, value=10.0, step=0.1)
        pH_range = np.linspace(pH_min, pH_max, 100)

    # Concentration input
    concentration = st.number_input("Enter drug concentration (molarity):", min_value=0.0, step=0.01)

    # Solubility calculation function
    def calculate_ionization(pKa, pH):
        ratio = 10 ** (pH - pKa)
        ionized = ratio / (1 + ratio) * 100
        non_ionized = 100 - ionized
        return ionized, non_ionized

    # Perform calculations and plot
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
