# maverick-analyst-financier

## Description
Proof of Concept (POC) d'un mini analyste financier IA. Ce projet connecte le LLM **LLaMA 4 Maverick** de Meta via l'API Replicate, avec un front simple codé sur **Replit**.

Il permet d'analyser la solidité financière d'une entreprise à partir de son **SIREN**, de son **statut (client/fournisseur)**, de son **historique de paiements**, et de **commentaires additionnels**, pour produire une **recommandation IA** structurée.

## Stack technique

- ✨ **Meta LLaMA 4 Maverick** via [Replicate](https://replicate.com/meta/llama-4-maverick-instruct)
- ⚙️ **API SocieteInfo** (données légales & financières)
- 🔢 **API Scores & Décisions** (score S&D, solvabilité, conformité)
- 🚀 **Replit** (Front MVP rapide)
- 💜 **Cursor** (IDE AI pour l'aide au dev Python)

## Fonctionnalités principales

- Entrée SIREN de l'entreprise
- Choix du rôle (Client / Fournisseur)
- Historique de paiement (aucun, bon, mauvais)
- Montant de l'encours
- Observations personnalisées
- Appel API SocieteInfo & Scores&Decisions pour enrichissement
- Requête envoyée à LLaMA 4 Maverick avec prompt contextualisé
- Réponse de l'IA structurée en 5 blocs :
  - 🔪 Score de risque
  - 📊 Analyse financière
  - ⏱️ Recommandation de paiement
  - 🔒 Analyse dirigeance / conformité
  - 🌍 Veille marché (si actu disponible)

## Installation locale (optionnelle)
```bash
# cloner le repo
https://github.com/kevinmameri/maverick-analyst-financier.git

cd maverick-analyst-financier

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le projet (par exemple avec Streamlit ou Flask)
streamlit run app.py
```

## Coût d'utilisation
**Modèle LLaMA 4 Maverick via Replicate (token-based)** :
- Input : $0.25 / 1M tokens
- Output : $0.95 / 1M tokens
- ≈ 1 265 analyses IA pour 1$

## Pourquoi ce projet ?
Tester rapidement la qualité d’un LLM sur des use cases **sectoriels** – ici, l’analyse financière B2B – en combinant **data premium**, **LLM** et **UX simplifiée**.

Idéal pour valider un **PMF** ou inspirer de futurs copilotes IA métiers low-cost.

---
✉️ Pour toute question, n'hésitez pas à me contacter ou ouvrir une issue !
