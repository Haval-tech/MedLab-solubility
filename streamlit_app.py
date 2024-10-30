import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt

# Function to fetch drug data from PubChem API
def get_drug_data(drug_name):
    # Search PubChem by drug name
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/IUPACName,pKa/JSON"
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        # Extract pKa if available
        if 'PropertyTable' in data:
            properties = data['PropertyTable']['Properties'][0]
            return properties.get('pKa', None)  # Returns the pKa value if available
    return None

# Streamlit app UI
st.title("Drug Solubility Simulation Tool")

# Add a search bar for API drug lookup
drug_name = st.text_input("Enter drug name to search for pKa:")

if drug_name:
    pKa = get_drug_data(drug_name)
    if pKa:
        st.write(f"Found pKa for {drug_name}: {pKa}")
        # Proceed with the rest of your solubility simulation using this pKa value
    else:
        st.write("pKa information not available for this drug.")
else:
    st.write("Enter a known pKa value to continue.")
    pKa = st.number_input("Enter pKa value manually:")

# Define parameters based on user input
if pKa:
    # Example pH range and simulation
    pH_range = np.linspace(1, 10, 100)

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
