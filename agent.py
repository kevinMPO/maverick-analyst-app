
import replicate
import os

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def analyze_company(company_data):
    replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

    prompt = f"""
Tu es un analyste financier IA. Voici les données d'une entreprise :

- Nom : {company_data['nom']}
- SIREN : {company_data['siren']}
- Forme juridique : {company_data['forme']}
- Ancienneté : {company_data['anciennete']}
- Chiffre d'affaires : {company_data['ca']}
- Résultat : {company_data['resultat']}
- Capitaux propres : {company_data['capitaux']}
- Score de solvabilité : {company_data['solvabilite']}

Donne-moi une recommandation :
1. Sur le risque crédit (faible, moyen, élevé)
2. Sur les délais de paiement recommandés (immédiat, 15j, 30j, 60j)
3. Un commentaire synthétique et professionnel.
"""

    output = replicate_client.run(
        "meta/meta-llama-3-70b-instruct",
        input={"prompt": prompt, "max_new_tokens": 500}
    )

    return "".join(output)
