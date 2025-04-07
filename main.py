
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from societeinfo import get_company_data
from scores import get_scores_decisions_data
from agent import analyze_company

st.set_page_config(page_title="Maverick Analyste Financier", page_icon="🧠")

st.title("🧠 Maverick – Analyse Financière IA")
st.markdown("Saisis le **nom de l'entreprise** pour analyser sa solidité financière et obtenir une recommandation IA.")

query = st.text_input("🔎 Nom de l'entreprise", placeholder="ex: Orange, SNCF, Doctolib...")
relation = st.selectbox("🤝 Rôle de l'entreprise", ["Client", "Fournisseur"])

if query:
    with st.spinner("📡 Récupération des données..."):
        data = get_company_data(query)
        if data and data.get('siren'):
            scores_data = get_scores_decisions_data(data['siren'])
            financial_data = get_financial_data(data['siren'], os.environ['SOCIETEINFO_API_KEY'])
            data.update(scores_data)
            data.update(financial_data)
        
    if data:
        st.success("✅ Données récupérées")

        col1, col2 = st.columns(2)
        with col1:
            historique = st.selectbox("📊 Historique de paiement (12 mois)", 
                ["Aucune expérience", "Nombreux retards", "Bonne expérience"])
            encours = st.number_input("💶 Montant de l'encours (€)", min_value=0)
        with col2:
            delai = st.selectbox("⏱️ Délai de paiement souhaité", 
                ["Comptant", "15 jours", "30 jours", "60 jours"])
        
        st.markdown("### 📝 Commentaires additionnels")
        commentaire = st.text_area("Ajoutez vos observations", height=100)
        
        info_paiement = st.text_area("ℹ️ Informations sur les paiements", height=100)
        evenements = st.text_area("📰 Événements récents", placeholder="Ex: AG, modifications statutaires...", height=100)
        
        # Un seul bouton d'analyse avec une clé unique
        if st.button("🔍 Analyser", key="analyze_button", disabled=not (query and historique and encours > 0)):
            data.update({
                "relation": relation,
                "historique": historique,
                "encours": encours,
                "delai_souhaite": delai,
                "commentaire": commentaire,
                "infoPaiement": info_paiement,
                "evenements_formates": evenements
            })

            with st.spinner("🧠 Analyse IA en cours..."):
                result = analyze_company(data)

            st.markdown("### 🤖 Recommandation Maverick")
            st.markdown(result)
    else:
        st.error("❌ Impossible de trouver cette entreprise.")
