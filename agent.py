
def analyze_company(company_data):
    """Analyse enrichie des données financières avec contexte commercial"""
    try:
        # Construction du prompt contextualisé
        prompt = f"""Tu es un analyste crédit IA expert. Analyse cette situation :

📊 Profil Entreprise :
- Nom : {company_data['nom']}
- SIREN : {company_data['siren']}
- Forme : {company_data['forme']}
- CA : {company_data['ca']} €
- Résultat : {company_data['resultat']} €
- Solvabilité : {company_data['solvabilite']}

💼 Contexte Commercial :
- Rôle : {company_data['relation']}
- Historique : {company_data['historique']}
- Encours : {company_data['encours']} €
- Délai souhaité : {company_data['delai_souhaite']}

"""
        # Analyse du risque basée sur la solvabilité
        if "Pas de risque" in company_data['solvabilite']:
            risk_level = "Faible 🟢"
            payment_advice = "60 jours"
        elif "Risque faible" in company_data['solvabilite']:
            risk_level = "Modéré 🟡"
            payment_advice = "30 jours"
        else:
            risk_level = "Élevé 🔴"
            payment_advice = "Comptant"

        # Formatage de la réponse
        analysis = f"""
### 📈 Synthèse Financière

> Je dois travailler avec **{company_data['nom']}** qui sera mon **{company_data['relation'].lower()}** 
> avec un historique de paiement : **{company_data['historique'].lower()}**
> Encours envisagé : **{company_data['encours']} €**

🎯 **Analyse du Risque**
- Niveau de risque : {risk_level}
- Délai recommandé : {payment_advice}
- Solvabilité actuelle : {company_data['solvabilite']}

💡 **Recommandation**
{get_recommendation(company_data, risk_level, payment_advice)}
"""
        return analysis

    except Exception as e:
        return f"⚠️ Erreur lors de l'analyse : {str(e)}"

def get_recommendation(data, risk, payment):
    """Génère une recommandation adaptée au contexte"""
    if "Faible" in risk:
        return f"Compte tenu de la bonne santé financière et du risque {risk}, vous pouvez accorder le délai de {payment}."
    elif "Modéré" in risk:
        return f"Une vigilance est recommandée. Privilégiez un délai de {payment} avec suivi régulier des paiements."
    else:
        return "⚠️ Le niveau de risque élevé suggère des conditions de paiement strictes ou des garanties complémentaires."
