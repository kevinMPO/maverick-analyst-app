import os

def analyze_company(company_data):
    """Analyse enrichie des données financières avec contexte commercial"""
    try:
        # Détermination du niveau de risque
        risk_level = get_risk_level(company_data)
        payment_advice = get_payment_advice(risk_level, company_data)

        analysis = f"""
> **{get_main_recommendation(risk_level, company_data)}**

---
🎯 **Analyse du Risque**
- Indiscore S&D : **{company_data.get('indiscore20', 'ND')}** / 20
- Niveau : **{risk_level}**
- Classe de risque : {company_data.get('classeRisque', 'ND')}
- Solvabilité : {company_data.get('solvabilite', 'ND')}

---
📊 **Analyse Financière**
- CA : {format_amount(company_data.get('ca'))}
- Résultat net : {format_amount(company_data.get('resultat'))}
- EBE : {format_amount(company_data.get('EBE'))}
- Fonds propres : {format_amount(company_data.get('FondsPr'))}
- Délai clients : {company_data.get('DelaiCli', 'ND')} jours
- Délai fournisseurs : {company_data.get('DelaiFour', 'ND')} jours

---
💳 **Recommandation Crédit**
- ✅ **Délai préconisé : {payment_advice}**
- 💶 Encours demandé : {format_amount(company_data.get('encours'))}
- 📈 Historique : {company_data.get('historique', 'ND')}
- ⚠️ Points de vigilance : {get_vigilance_points(company_data)}

---
👔 **Gouvernance & Conformité**
- Dirigeance : {company_data.get('AnalyseDirigeance', 'ND')}
- Score conformité : {company_data.get('ScoreConfor', 'ND')}
- Analyse conformité : {company_data.get('AnalyseConfor', 'ND')}

---
📰 **Événements Significatifs**
{company_data.get('evenements_formates', 'Aucun événement significatif à signaler.')}
"""
        return analysis
    except Exception as e:
        return f"⚠️ Erreur lors de l'analyse : {str(e)}"

def get_risk_level(data):
    """Détermine le niveau de risque avec emoji"""
    if "Pas de risque" in data.get('solvabilite', ''):
        return "Faible 🟢"
    elif "Risque faible" in data.get('solvabilite', ''):
        return "Modéré 🟡"
    return "Élevé 🔴"

def get_payment_advice(risk_level, data):
    """Détermine le délai de paiement recommandé"""
    if risk_level == "Faible 🟢" and data.get('historique') == "Bonne expérience":
        return "60 jours"
    elif risk_level == "Modéré 🟡":
        return "30 jours avec suivi"
    return "Comptant"

def get_main_recommendation(risk_level, data):
    """Génère la recommandation principale"""
    encours = data.get('encours', 0)
    if "Faible" in risk_level:
        return f"Favorable à l'encours de {format_amount(encours)}"
    elif "Modéré" in risk_level:
        return f"Accord sous conditions pour {format_amount(encours)}"
    return "Refus conseillé - Risque élevé"

def get_vigilance_points(data):
    """Identifie les points de vigilance"""
    points = []
    if data.get('DelaiCli', 0) > 60:
        points.append("Délais clients élevés")
    if data.get('FondsPr', 0) < 0:
        points.append("Fonds propres négatifs")
    return " | ".join(points) if points else "RAS"

def format_amount(amount):
    """Formate les montants en k€ ou M€"""
    try:
        if not amount or amount == "ND":
            return "ND"
        amount = float(amount)
        if amount >= 1000000:
            return f"{amount/1000000:.1f}M€"
        elif amount >= 1000:
            return f"{amount/1000:.0f}k€"
        return f"{amount:.0f}€"
    except:
        return "ND"