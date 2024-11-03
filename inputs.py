import streamlit as st

def get_user_inputs():
    pKa = st.number_input("Enter the pKa of the drug:", min_value=0.0, max_value=14.0, step=0.1)
    concentration_mg = st.number_input("Enter drug concentration (mg):", min_value=0.0, step=0.1)
    
    environments = {
        "Stomach": (1, 3),
        "Duodenum": (5, 6),
        "Jejunum": (6, 7),
        "Ileum": (7, 8)
    }
    
    st.write("### Select the Environment(s)")
    selected_env = [env for env in environments.keys() if st.checkbox(env)]
    
    return pKa, concentration_mg, selected_env
