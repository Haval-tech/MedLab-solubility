# solubility_simulation.py
import requests

def get_autocomplete_suggestions(query):
    """Fetch autocomplete suggestions from PubChem for a given query."""
    autocomplete_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/compound/{query}/JSON?limit=10"
    response = requests.get(autocomplete_url)
    if response.status_code == 200:
        data = response.json()
        if "dictionary_terms" in data:
            return data["dictionary_terms"]["compound"]
    return []
