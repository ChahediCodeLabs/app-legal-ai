# app_legal.py
import streamlit  as st
import tempfile
import os
from logic_legal import analyser_contrat

st.set_page_config(page_title="Legal AI")
st.title("⚖️ Analyseur de Contrats")

role = st.text_input("Mon rôle", "Freelance")
adverse = st.text_input("Partie adverse", "Client")
uploaded_file = st.file_uploader("Contrat PDF", type=["pdf"])

if st.button("🔍 Analyser") and uploaded_file:
    # Sauvegarde temporaire sur le disque
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    with st.spinner("Lecture du document..."):
        res = analyser_contrat(tmp_path, "application/pdf", role, adverse)
        st.markdown(res)
    
    os.remove(tmp_path) # Nettoyage