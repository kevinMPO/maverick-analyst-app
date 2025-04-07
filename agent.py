
import os

def analyze_company(company_data):
    """Analyse les données financières d'une entreprise et retourne une synthèse structurée"""
    
    try:
        # Extraction des indicateurs clés
        ca = company_data['ca']
        resultat = company_data['resultat'] 
        solvabilite = company_data['solvabilite']
        
        # Logique d'analyse simplifiée
        if "Pas de risque" in solvabilite:
            risk_score = "2/10 🟢"
            payment_terms = "60 jours"
        elif "Risque faible" in solvabilite:
            risk_score = "4/10 🟡"
            payment_terms = "30 jours"
        else:
            risk_score = "7/10 🔴"
            payment_terms = "15 jours"

        # Formatage de la réponse
        analysis = f"""🔍 Analyse Financière IA — Synthèse

📌 Risque Crédit : {risk_score}
⏳ Paiement recommandé : {payment_terms}

💬 Commentaire :
{company_data['nom']} présente un chiffre d'affaires de {ca}€ avec un résultat net de {resultat}€. 
Le niveau de solvabilité indique : {solvabilite}.

📣 Conseil IA :
{"Entreprise fiable, délais standards conseillés." if "Pas de risque" in solvabilite else "Surveillance recommandée des délais de paiement."}
"""
        return analysis

    except Exception as e:
        return f"⚠️ Erreur lors de l'analyse : {str(e)}"
