import streamlit as st
import requests
import os
from streamlit_option_menu import option_menu

# Load webhook URL from environment variable
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

st.set_page_config(page_title="Newsletter Contributor", page_icon="📰")

# -----------------------------
# Sidebar Navigation
# -----------------------------
with st.sidebar:
    page = option_menu(
        menu_title="Stay Tuned",
        options=["Contribution", "Espace Expert"],
        icons=["newspaper", "person-badge"],
        default_index=0,
    )
# -----------------------------
# PAGE 1 : Contribution
# -----------------------------
if page == "Contribution":
    st.title("📰 Contribution à la Newsletter - Stay Tuned")
    st.write("Bienvenue ! Remplis le formulaire ci-dessous pour contribuer à la prochaine édition.")

    with st.form("newsletter_form"):
        source = st.text_input("Source / Lien de l'article")
        source_name = st.text_input("Nom de la source (ex: Le Monde, YouTube, etc.)")
        source_type = st.selectbox("Type de source", ["URL", "Vidéo", "RSS"])
        niveau = st.selectbox("Niveau de difficulté", ["Débutant", "Intermédiaire", "Avancé"])
        want_to_be_credited = st.checkbox("Je souhaite être crédité(e) dans la newsletter", value=False)

        contributor = st.text_input("Nom du contributeur") if want_to_be_credited else ""
        email = st.text_input("Adresse e-mail (optionnelle)") if want_to_be_credited else ""

        submitted = st.form_submit_button("Envoyer")

    if submitted:
        data = {
            "url": source,
            "source_name": source_name,
            "source_type": source_type,
            "niveau": niveau,
            "contributor": contributor if want_to_be_credited else "Anonyme",
            "email": email if want_to_be_credited else "",
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


# -----------------------------
# PAGE 2 : Espace Expert
# -----------------------------
elif page == "Espace Expert":
    st.title("🧠 Espace Expert")
    st.write("Cette section sera utilisée pour gérer les experts, leurs tags, leurs topics, etc.")

    st.info("🔧 Cette page n'est pas encore configurée. Tu peux ajouter des fonctionnalités ici !")

    st.subheader("Exemple : Indiquer son/ses expertises")

    with st.form("expert_form"):
        expert_name = st.text_input("Nom de l'expert")
        expertise_tags = st.multiselect("Tags d'expertise", ["DBT", "Snowflake", "Python", "ML", "Data Viz"])
        submitted_expert = st.form_submit_button("Enregistrer")

    if submitted_expert:
        st.success("Expert enregistré (exemple) !")
        st.json({"expert_name": expert_name, "expertise": expertise_tags})
