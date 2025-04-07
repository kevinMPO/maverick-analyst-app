
import requests
import os

API_KEY = os.getenv("SOCIETEINFO_API_KEY")
print(f"API Key loaded: {'Yes' if API_KEY else 'No'}")

def get_financial_data(registration_number, api_key):
    url = f"https://societeinfo.com/app/rest/api/v2/financial/statements.json/{registration_number}"
    params = {"key": api_key}
    
    try:
        res = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=5)
        if res.status_code == 200:
            data = res.json().get("result", {})
            latest = data.get("statements", [{}])[0] if data.get("statements") else {}
            
            return {
                "evolution_ca": latest.get("turnover_var"),
                "marge_nette": latest.get("net_margin"),
                "taux_ebe": latest.get("ebitda_margin"),
                "gearing": latest.get("gearing"),
                "tresorerie": latest.get("cash"),
                "bfr": latest.get("working_capital"),
                "altman_score": latest.get("altman_score"),
                "conan_holder": latest.get("conan_holder")
            }
        print(f"Erreur API financials: {res.status_code}")
        return {}
    except Exception as e:
        print(f"Erreur lors de l'appel financials: {str(e)}")
        return {}

def get_company_data(query):
    # Supporte la recherche par SIREN/SIRET ou nom d'entreprise
    url = "https://societeinfo.com/app/rest/api/v2/company.json"
    
    # Si le query est numérique (SIREN/SIRET), on utilise registration_number
    if query.isdigit():
        params = {
            "key": API_KEY,
            "registration_number": query
        }
    else:
        # Sinon on fait une recherche par nom
        params = {
            "key": API_KEY,
            "q": query
        }

    try:
        res = requests.get(
            url, 
            params=params, 
            headers={"Accept": "application/json"}, 
            timeout=5
        )
        print(f"API Response status: {res.status_code}")
        print(f"API Response content: {res.text[:200]}")  # Log des 200 premiers caractères

        if res.status_code == 401:
            print("Erreur d'authentification: Clé API invalide")
            return None
        elif res.status_code == 404:
            print("Entreprise non trouvée")
            return None
        elif res.status_code == 429:
            print("Trop de requêtes, veuillez réessayer plus tard")
            return None
            
        res.raise_for_status()
        data = res.json()
        
        if not data.get("success") or "result" not in data:
            print("Format de réponse invalide")
            return None

        org = data["result"]["organization"]
        fin = data["result"].get("financials", {})

        return {
            "nom": org.get("name"),
            "siren": org.get("registration_number"),
            "forme": org.get("legal", {}).get("name"),
            "creation": org.get("creation_date"),
            "capital": org.get("capital"),
            "ca": fin.get("last_sales", "ND"),
            "resultat": fin.get("last_profit", "ND"),
            "effectif": fin.get("last_staff", "ND"),
            "solvabilite": org.get("risk", {}).get("risk_level_description", "ND"),
            "anciennete": org.get("age", "ND")
        }

    except requests.RequestException as e:
        print(f"Erreur de connexion à Societeinfo: {str(e)}")
        return None
    except Exception as e:
        print(f"Erreur inattendue: {str(e)}")
        return None
