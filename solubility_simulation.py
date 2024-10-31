# solubility_simulation.py
import numpy as np
import requests

def get_drug_data(drug_name):
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/IUPACName,pKa/JSON"
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        if 'PropertyTable' in data:
            properties = data['PropertyTable']['Properties'][0]
            return properties.get('pKa', None)
    return None

def calculate_ionization(pKa, pH):
    ratio = 10 ** (pH - pKa)
    ionized = ratio / (1 + ratio) * 100
    return ionized

def get_pH_ranges(selected_env, environments):
    pH_ranges = []
    for env in selected_env:
        pH_min, pH_max = environments[env]
        pH_ranges.extend(np.linspace(pH_min, pH_max, 50))
    return pH_ranges

def get_autocomplete_suggestions(query):
    """Fetch autocomplete suggestions from PubChem for a given query."""
    autocomplete_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/compound/{query}/JSON?limit=10"
    response = requests.get(autocomplete_url)
    if response.status_code == 200:
        data = response.json()
        if "dictionary_terms" in data:
            return data["dictionary_terms"]["compound"]
    return []
