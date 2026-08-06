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

    submitted = st.form_submit_button("Envoyer")

# Enregistrement dans Supabase
if submitted:
    if nom and prenom and email:

        data_membre = {
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "telephone": telephone
        }

        supabase.table("membres").insert(data_membre).execute()

        st.success("Votre préinscription a été envoyée avec succès !")

    else:
        st.error("Veuillez remplir au minimum nom, prénom et email.")
