
def analyze_company(company_data):
    """Analyse enrichie des données financières avec contexte commercial"""
    try:
        # Construction du prompt contextualisé
        prompt = f"""
Tu es un analyste crédit IA, expert en finance B2B. Tu agis comme un analyste senior dans un cabinet de notation ou une direction financière. Ta mission est d'émettre une recommandation de crédit claire, fiable et contextualisée à partir des éléments suivants :

📄 **Profil Entreprise**
- Nom : {company_data['nom']}
- SIREN : {company_data['siren']}
- Forme juridique : {company_data.get('forme', 'ND')}
- Ancienneté : {company_data.get('anciennete', 'ND')}
- Chiffre d'affaires : {company_data.get('ca', 'ND')} €
- Résultat net : {company_data.get('resultat', 'ND')} €
- Score de solvabilité : {company_data.get('solvabilite', 'ND')}

💼 **Contexte Commercial**
- Cette entreprise est mon : **{company_data['relation']}**
- Historique de paiement sur 12 mois : **{company_data['historique']}**
- Encours envisagé : **{company_data['encours']} €**
- Délai souhaité : **{company_data['delai_souhaite']}**

---

✍️ **Ta tâche** :
Rédige une synthèse professionnelle et structurée en **markdown**, avec 4 sections :
1. **Analyse financière** (solvabilité, rentabilité, structure)
2. **Évaluation du risque crédit** (faible, moyen, élevé)
3. **Recommandation de délai de paiement** (comptant / 30j / 60j)
4. **Conclusion synthétique**

🧠 Ta réponse doit être :
- Synthétique
- Impactante
- Orientée action
- Utilisable en contexte réel
- Utilise des bullet points, emojis pour lisibilité

Commence toujours ta réponse par :  
> **Je recommande que...**
"""
        # Analyse du risque basée sur la solvabilité
        if "Pas de risque" in company_data.get('solvabilite', ''):
            risk_level = "Faible 🟢"
            payment_advice = "60 jours"
        elif "Risque faible" in company_data.get('solvabilite', ''):
            risk_level = "Modéré 🟡"
            payment_advice = "30 jours"
        else:
            risk_level = "Élevé 🔴"
            payment_advice = "Comptant"

        # Formatage de la réponse
        analysis = f"""### 📊 Analyse Financière
- Chiffre d'affaires : **{company_data.get('ca', 'ND')}** €
- Résultat net : **{company_data.get('resultat', 'ND')}** €
- Solvabilité : **{company_data.get('solvabilite', 'ND')}**

### 🎯 Évaluation du Risque
- Niveau : **{risk_level}**
- Délai recommandé : **{payment_advice}**
- Historique : {company_data['historique']}

### 💡 Recommandation
{get_recommendation(company_data, risk_level, payment_advice)}

### 🤝 Conclusion
> **Je recommande que** nous travaillions avec **{company_data['nom']}** en tant que **{company_data['relation'].lower()}** avec un délai de paiement de **{payment_advice}** pour un encours de **{company_data['encours']}** €.
"""
        return analysis

    except Exception as e:
        return f"⚠️ Erreur lors de l'analyse : {str(e)}"

def get_recommendation(data, risk, payment):
    """Génère une recommandation adaptée au contexte"""
    if "Faible" in risk:
        return f"✅ Compte tenu de la bonne santé financière et du risque {risk}, vous pouvez accorder le délai de {payment}."
    elif "Modéré" in risk:
        return f"⚠️ Une vigilance est recommandée. Privilégiez un délai de {payment} avec suivi régulier des paiements."
    else:
        return "🚫 Le niveau de risque élevé suggère des conditions de paiement strictes ou des garanties complémentaires."
