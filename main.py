from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from societeinfo import get_company_data
from agent import analyze_company

st.set_page_config(page_title="Maverick Analyste Financier", page_icon="🧠")

st.title("🧠 Maverick – Analyse Financière IA")
st.markdown("Saisis le **nom de l'entreprise** pour analyser sa solidité financière et obtenir une recommandation IA.")

col1, col2 = st.columns(2)
with col1:
    query = st.text_input("🔎 Nom de l'entreprise", placeholder="ex: Orange, SNCF, Doctolib...")
with col2:
    relation = st.selectbox("🤝 Rôle de l'entreprise", ["Client", "Fournisseur"])

analyze_button = st.button("🔍 Analyser")
if analyze_button:
    if query:
        with st.spinner("📡 Récupération des données..."):
            data = get_company_data(query)

        if data:
            st.success("✅ Données récupérées")

            col3, col4 = st.columns(2)
            with col3:
                historique = st.selectbox("📊 Historique de paiement (12 mois)", 
                    ["Aucune expérience", "Nombreux retards", "Bonne expérience"])
                encours = st.number_input("💶 Montant de l'encours (€)", min_value=0)
            with col4:
                delai = st.selectbox("⏱️ Délai de paiement souhaité", 
                    ["Comptant", "15 jours", "30 jours", "60 jours"])

            data.update({
                "relation": relation,
                "historique": historique,
                "encours": encours,
                "delai_souhaite": delai
            })

            with st.spinner("🧠 Analyse IA en cours..."):
                result = analyze_company(data)

            st.markdown("### 🤖 Recommandation Maverick")
            st.markdown(result)
        else:
            st.error("❌ Impossible de trouver cette entreprise.")