
import replicate
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

def analyze_company(company_data):
    prompt = f"""
Tu es un analyste crédit IA de niveau senior. Tu dois rendre une **synthèse complète et professionnelle** à partir des données suivantes, sous forme de 5 blocs **structurés et argumentés**.

---

📌 **Contexte entreprise**
- Nom : {company_data.get('nom')}
- SIREN : {company_data.get('siren')}
- Secteur : {company_data.get('LibSecteur')}
- Forme juridique : {company_data.get('forme')}
- Dirigeance : {company_data.get('AnalyseDirigeance', 'ND')}

📂 **Relation commerciale**
- Rôle : {company_data.get('role')}
- Historique paiement : {company_data.get('historique')}
- Encours actuel : {company_data.get('encours')} €
- Délai souhaité : {company_data.get('delaiSouhaite')}
- Commentaire utilisateur : {company_data.get('commentaire')}
- Info paiement : {company_data.get('paiement_info')}

---

🎯 **1. Score de Risque**

- Classe risque : {company_data.get('classeRisque')} /10
- Indiscore S&D : {company_data.get('Indiscore20')} /20
- Indiscore secteur : {company_data.get('Indiscore20_secteur')}
- Score conformité : {company_data.get('ScoreConfor')} ({company_data.get('AnalyseConfor')})
- Code couleur recommandé (🟢🟡🔴)

---

📊 **2. Analyse Financière Avancée**

Performance & Rentabilité :
- CA : {company_data.get('ca')} € | Évolution : {company_data.get('evolution_ca', 'ND')}%
- Résultat net : {company_data.get('resultat')} € | Marge nette : {company_data.get('marge_nette', 'ND')}%
- EBE : {company_data.get('EBE')} € | Marge EBE : {company_data.get('taux_ebe', 'ND')}%
- ROE : {company_data.get('return_on_equity', 'ND')}% | ROA : {company_data.get('return_on_assets', 'ND')}%

Structure Financière :
- Fonds propres : {company_data.get('FondsPr')} € | Gearing : {company_data.get('gearing', 'ND')}
- Trésorerie : {company_data.get('tresorerie', 'ND')} € | BFR : {company_data.get('bfr', 'ND')} €
- Ratio liquidité : {company_data.get('current_ratio', 'ND')} | Quick ratio : {company_data.get('quick_ratio', 'ND')}
- Taux endettement : {company_data.get('debt_ratio', 'ND')}%

Gestion & Exploitation :
- Délai clients : {company_data.get('DelaiCli')} j | Fournisseurs : {company_data.get('DelaiFour')} j
- Rotation stocks : {company_data.get('stock_rotation', 'ND')} j
- BFR en jours CA : {company_data.get('working_capital_days', 'ND')} j

Scores & Prédictifs :
- Score Altman : {company_data.get('altman_score', 'ND')} | Conan-Holder : {company_data.get('conan_holder', 'ND')}
- Afdcc1 : {company_data.get('Afdcc1')} | Score Z : {company_data.get('z_score', 'ND')}
- Probabilité défaut : {company_data.get('default_probability', 'ND')}%

---

💳 **3. Recommandation Paiement**

- Délai recommandé (comptant / 30j / 60j)
- Justification claire (solvabilité, historique, encours, structure)
- Mention de toute alerte ou réserve éventuelle

---

👔 **4. Gouvernance & Conformité**

- Dirigeance : {company_data.get('AnalyseDirigeance')}
- Conformité : {company_data.get('AnalyseConfor')} ({company_data.get('ScoreConfor')} /100)
- Remarques éventuelles sur les encours, signaux faibles ou alertes légales

---

📰 **5. Veille Marché**

{company_data.get('evenement_info', '- Aucun événement récent détecté.')}

---

"""Améliorer Prompt + Prévoir crewai"""
🧠 **Analyse libre Maverick**

Tu es libre d'apporter **une réflexion complémentaire**, comme un expert humain :
- Un angle d'analyse original ?
- Une alerte ?
- Une opportunité ?
- Un commentaire sur le timing ou le secteur ?
**Agis en stratège. Surprends-moi.**
"""

    output = replicate_client.run(
        "meta/llama-4-maverick-instruct",
        input={"prompt": prompt, "max_new_tokens": 800}
    )

    return "".join(output)
