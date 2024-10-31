# streamlit_app.py
import streamlit as st
from solubility_simulation import get_drug_data, calculate_ionization, get_pH_ranges, get_autocomplete_suggestions
from plot_settings import plot_solubility
from layout_settings import setup_layout

# Set up the layout
setup_layout()

# Title
st.title("MedLab Drug Solubility Simulation Tool")

# Choose input mode
input_mode = st.radio("Choose input mode:", ["API Search", "Manual Input"])

# Initialize session state for query and suggestions
if "query" not in st.session_state:
    st.session_state.query = ""
if "suggestions" not in st.session_state:
    st.session_state.suggestions = []

# Autocomplete and API Search
pKa = None
selected_name = None

if input_mode == "API Search":
    # Search bar with autocomplete functionality
    query = st.text_input("Enter drug or substance name:", key="query")
    
    # Update suggestions only when the query changes
    if query and query != st.session_state.query:
        st.session_state.query = query
        st.session_state.suggestions = get_autocomplete_suggestions(query)

    # Display suggestions as clickable buttons
    if st.session_state.suggestions:
        st.write("Did you mean:")
        for suggestion in st.session_state.suggestions:
            if st.button(suggestion):  # Display each suggestion as a button
                selected_name = suggestion
                pKa = get_drug_data(selected_name)
                if pKa:
                    st.write(f"Found pKa for {selected_name}: {pKa}")
                else:
                    st.write("pKa information not available for this drug.")
                st.session_state.suggestions = []  # Clear suggestions after selection
                break  # Exit loop after selection
else:
    # Manual input mode
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
