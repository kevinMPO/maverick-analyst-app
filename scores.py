
import requests
import base64
import os

SD_TOKEN = os.getenv("SD_TOKEN")

def get_scores_decisions_data(siren):
    """Récupère les données depuis l'API Scores & Décisions"""
    url = f"https://ws.scores-decisions.com/api/V1/service/entreprise/act/getIndiScore/{siren}"
    headers = {
        "Authorization": f"Basic {SD_TOKEN}",
        "Accept": "application/json"
    }
    
    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print(f"Erreur S&D : {res.status_code}")
            return {}
        
        data = res.json()
        return {
            "indiscore20": data.get("Indiscore20"),
            "indiscore20_secteur": data.get("Indiscore20_secteur"),
            "AnalyseDirigeance": data.get("AnalyseDirigeance"),
            "ScoreConfor": data.get("ScoreConfor"),
            "AnalyseConfor": data.get("AnalyseConfor"),
            "encours_sd": data.get("encours"),
            "classeRisque": data.get("classeRisque"),
            "FondsPr": data.get("Bilans", [{}])[0].get("FondsPr"),
            "EBE": data.get("Bilans", [{}])[0].get("EBE"),
            "DelaiCli": data.get("Bilans", [{}])[0].get("DelaiCli"),
            "DelaiFour": data.get("Bilans", [{}])[0].get("DelaiFour"),
            "Afdcc1": data.get("Afdcc1"),
            "ConanH": data.get("ConanH")
        }
    except Exception as e:
        print(f"Erreur lors de l'appel à S&D: {str(e)}")
        return {}
