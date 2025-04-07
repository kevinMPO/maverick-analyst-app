import replicate
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def analyze_company(company_data):
    replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

    prompt = f"""
Tu es un analyste financier IA de haut niveau, spécialisé dans l’évaluation du risque crédit des PME françaises.

Voici les données de l'entreprise :

🏢 Nom : {company_data['nom']}
🔢 SIREN : {company_data['siren']}
🏛 Forme juridique : {company_data['forme']}
📅 Date de création : {company_data['creation']}
📊 Chiffre d'affaires : {company_data['ca']} €
💰 Résultat net : {company_data['resultat']} €
📈 Capitaux propres : {company_data.get('capitaux', 'ND')} €
👥 Effectif : {company_data.get('effectif', 'ND')}
💳 Solvabilité : {company_data['solvabilite']}
📆 Ancienneté estimée : {company_data['anciennete']}

🔍 Analyse attendue :

1. Score de **risque crédit** sur 10 + 🔴🟡🟢
2. **Recommandation de délai de paiement** : immédiat / 15j / 30j / 60j
3. Synthèse d’expert (2-3 phrases pro, claires et sans jargon inutile)
4. Conseil IA (précaution, alerte ou bonne pratique selon le cas)

Réponds de façon lisible, structurée, avec des emojis si utiles, et une vraie valeur ajoutée.
"""

    output = replicate_client.run(
        "meta/llama-4-maverick-instruct",
        input={"prompt": prompt, "max_new_tokens": 600}
    )

    return "".join(output)
