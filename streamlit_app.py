import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt

# Function to fetch drug data from PubChem API
def get_drug_data(drug_name):
    # Search PubChem by drug name
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/IUPACName,pKa/JSON"
    response = requests.get(search_url)
    if response.status_code == 200:  # Added the missing colon here
        data = response.json()
        # Extract pKa if available
        if 'PropertyTable' in data:
            properties = data['PropertyTable']['Properties'][0]
            return properties.get('pKa', None)  # Returns the pKa value if available
    return None

# Streamlit app UI
st.title("MedLab Drug Solubility Simulation Tool")

# Choose input mode
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

# Environment Selection with checkboxes
st.sidebar.header("Choose Environment")
environments = {
    "Stomach": (1, 3),
    "Duodenum": (5, 6),
    "Jejunum": (6, 7),
    "Ileum": (7, 8)
}
selected_env = [env for env in environments.keys() if st.sidebar.checkbox(env)]

# Placeholder for solubility calculation and plotting
if pKa and selected_env:
    # Set up pH ranges based on selected environments
    pH_ranges = []
    for env in selected_env:
        pH_min, pH_max = environments[env]
        pH_ranges.extend(np.linspace(pH_min, pH_max, 50))

    # Calculate solubility for each pH
    def calculate_ionization(pKa, pH):
        ratio = 10 ** (pH - pKa)
        ionized = ratio / (1 + ratio) * 100
        return ionized

    ionized_percentages = [calculate_ionization(pKa, pH) for pH in pH_ranges]
    time_range = np.linspace(0, len(ionized_percentages), len(ionized_percentages))

    # Plot the graph
    fig, ax = plt.subplots()
    ax.plot(time_range, ionized_percentages, label='Solubility (%)', color='blue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Solubility Percentage')
    ax.set_title("Solubility Percentage over Time")
    st.pyplot(fig)
