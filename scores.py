
import requests
import base64
import os

SD_TOKEN = os.getenv("SD_TOKEN")

def get_scores_decisions_data(siren):
    """Récupère les données depuis l'API Scores & Décisions"""
    url = f"https://ws.scores-decisions.com/api/V1/service/entreprise/act/getIndiScore/?siren={siren}"
    headers = {
        "Authorization": f"Basic {base64.b64encode(SD_TOKEN.encode()).decode()}",
        "Accept": "application/json"
    }
    
    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print(f"Erreur S&D : {res.status_code}")
            return {}
        
        data = res.json().get("body", {})
        bilans = data.get("Bilans", [{}])[0] if data.get("Bilans") else {}
        return {
            "indiscore20": data.get("Indiscore20"),
            "indiscore20_secteur": data.get("Indiscore20Secteur"),
            "AnalyseDirigeance": data.get("AnalyseDirigeance"),
            "ScoreConfor": data.get("ScoreConfor"),
            "AnalyseConfor": data.get("AnalyseConfor"),
            "encours_sd": data.get("encours"),
            "classeRisque": data.get("classeRisque"),
            "FondsPr": data.get("FondsPr"),
            "EBE": data.get("EBE"),
            "DelaiCli": round(float(bilans.get("DelaiCli", 0))) if bilans.get("DelaiCli") else None,
            "DelaiFour": round(float(bilans.get("DelaiFour", 0))) if bilans.get("DelaiFour") else None,
            "Afdcc1": data.get("Afdcc1"),
            "ConanH": data.get("ConanH")
        }
    except Exception as e:
        print(f"Erreur lors de l'appel à S&D: {str(e)}")
        return {}
