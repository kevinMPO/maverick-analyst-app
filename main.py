
import streamlit as st
from societeinfo import get_company_data
from agent import analyze_company

st.set_page_config(page_title="Maverick Analyste Financier", page_icon="🧠")

st.title("🧠 Maverick – Analyse Financière IA")
st.markdown("Saisis le **nom de l'entreprise** pour analyser sa solidité financière, son risque crédit, et obtenir une recommandation IA.")

query = st.text_input("🔎 Nom de l'entreprise à analyser", placeholder="ex : Orange, SNCF, Doctolib...")

if st.button("Analyser") and query:
    with st.spinner("📡 Récupération des données..."):
        data = get_company_data(query)
    
    if data:
        st.success("✅ Données récupérées avec succès.")
        st.json(data)

        with st.spinner("🧠 Analyse IA en cours..."):
            result = analyze_company(data)
        
        st.markdown("### 🤖 Recommandation Maverick")
        st.write(result)
    else:
        st.error("❌ Impossible de trouver cette entreprise.")
