import streamlit as st
from supabase import create_client
from datetime import datetime

# Connexion Supabase
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("Préinscription au Club Canin")

with st.form("preinscription_form"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")

    submitted = st.form_submit_button("Envoyer")

if submitted:
    data = {
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "telephone": telephone,
        "date_preinscription": datetime.now().isoformat(),
        "statut": "en_attente"
    }

    supabase.table("preinscription").insert(data).execute()

    st.success("Votre préinscription a été envoyée avec succès !")
