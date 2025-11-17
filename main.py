import streamlit as st
import requests

WEBHOOK_URL = "http://localhost:5678/webhook-test/e5780172-1bf0-479f-8211-b90e557f64c6"

st.set_page_config(page_title="Newsletter Contributor", page_icon="📰")

st.title("📰 Contribution à la Newsletter - Stay Tuned")
st.write("Bienvenue ! Remplis le formulaire ci-dessous pour contribuer à la prochaine édition.")

with st.form("newsletter_form"):
    source = st.text_input("Source / Lien de l'article")
    source_type = st.selectbox("Type de source", ["Article", "url", "Vidéo", "Podcast", "Autre"])
    topic = st.selectbox("Sujet principal", ["DBT", "Science", "Machine Learning", "Autre"])
    niveau = st.selectbox("Niveau de difficulté", ["Débutant", "Intermédiaire", "Avancé"])
    submitted = st.form_submit_button("Envoyer")

    want_to_be_credited = st.checkbox("Je souhaite être crédité(e) dans la newsletter", value=False)

    if want_to_be_credited:
        author = st.text_input("Nom à afficher pour le crédit")
        email = st.text_input("Adresse e-mail (optionnelle)")

if submitted:

    # Les données envoyées au webhook
    data = {
        "url": source,
        "source_type": source_type,
        "topic": topic,
        "niveau": niveau,
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)

        if response.status_code in [200, 201]:
            st.success("🎉 Merci ! Ta contribution a été envoyée.")
        else:
            st.error(f"❌ Erreur lors de l’envoi au webhook : {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

    st.json(data)
