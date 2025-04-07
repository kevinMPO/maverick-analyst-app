
import requests
import os

API_KEY = os.getenv("SOCIETEINFO_API_KEY")

def get_company_data(query):
    url = "https://societeinfo.com/app/rest/api/v2/company"
    params = {"key": API_KEY, "q": query, "limit": 1}
    res = requests.get(url, params=params)

    if res.status_code == 200:
        data = res.json().get("companies", [])[0]
        return {
            "nom": data.get("name"),
            "siren": data.get("siren"),
            "creation": data.get("establishment", {}).get("dateCreation"),
            "forme": data.get("legalForm"),
            "dirigeant": data.get("lastDirigeant"),
            "ca": data.get("financials", {}).get("last", {}).get("ca", "ND"),
            "resultat": data.get("financials", {}).get("last", {}).get("result", "ND"),
            "capitaux": data.get("financials", {}).get("last", {}).get("capitauxPropres", "ND"),
            "solvabilite": data.get("financialRating", {}).get("score", "ND"),
            "anciennete": data.get("years", "ND")
        }
    else:
        return None
