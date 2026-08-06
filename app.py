import streamlit as st
from supabase import create_client, Client

# Connexion Supabase
url = st.secrets["supabase_url"]
key = st.secrets["supabase_key"]
supabase: Client = create_client(url, key)

st.title("Préinscription au Club Canin")
st.write("Veuillez remplir le formulaire ci-dessous pour vous préinscrire.")

# Formulaire
with st.form("preinscription_form"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")

    nom_chien = st.text_input("Nom du chien")
    race_chien = st.text_input("Race du chien")
    age_chien = st.number_input("Âge du chien (en années)", min_value=0, max_value=30)

    submitted = st.form_submit_button("Envoyer")

# Enregistrement dans Supabase
if submitted:
    if nom and prenom and email:

        # 1️⃣ Insertion du membre (SANS données du chien)
        data_membre = {
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "telephone": telephone
        }

        response = supabase.table("membres").insert(data_membre).execute()
        membre_id = response.data[0]["id"]

        # 2️⃣ Insertion du chien uniquement si les champs sont remplis
        if nom_chien and race_chien and age_chien:
            data_chien = {
                "membre_id": membre_id,
                "nom_chien": nom_chien,
                "race_chien": race_chien,
                "age_chien": age_chien
            }
            supabase.table("chiens").insert(data_chien).execute()

        st.success("Votre préinscription a été envoyée avec succès !")

    else:
        st.error("Veuillez remplir au minimum nom, prénom et email.")
