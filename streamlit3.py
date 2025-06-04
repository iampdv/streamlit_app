import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu # Import manquant ajouté

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP', # En production, les mots de passe doivent être hachés
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP', # En production, les mots de passe doivent être hachés
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Initialisation de l'authentificateur
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",         # Le nom du cookie, un str quelconque
    "cookie_key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# Tentative de connexion de l'utilisateur
authenticator.login()

# Définition de la fonction pour la page d'accueil
def accueil():
    st.title("Bienvenue sur ma page")
    st.image("https://cdn.shopify.com/s/files/1/0780/2886/5873/files/DALL_E_2024-06-19_20.56.27_-_A_highly_realistic_image_of_a_stereotypical_beauf_from_France._The_character_is_a_middle-aged_man_with_a_beer_belly_wearing_a_sleeveless_tank_top_480x480.webp?v=1718823431")

# Définition de la fonction pour la page des photos de chat
def chat():
    st.title("Bienvenue dans l'album de mon chat 🐈!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.istockphoto.com/id/1313021528/fr/photo/chasse-de-chat-%C3%A0-la-souris-%C3%A0-la-maison-visage-birman-de-chat-avant-plan-rapproch%C3%A9-dattaque.jpg?s=612x612&w=0&k=20&c=gqKaQDXBLj0pZBgEjEajKIItl32QaYd3GrVo7Nl2OYA=")
    with col2:
        st.image("https://media.istockphoto.com/id/820785498/fr/photo/mignon-chaton-jouant.jpg?s=612x612&w=0&k=20&c=AlaMxg0Ydk8K2gqUiQXkPfiQkXF8lvdEYVWPVN3rBr8=")
    with col3:
        st.image("https://media.istockphoto.com/id/537716191/fr/photo/chat-jouant.jpg?s=612x612&w=0&k=20&c=238IgC0rmO0pKv0g9Wk6TZeGrrsmmZaDR-aopWNzXuo=")
    

# Logique de rendu conditionnel basée sur l'état d'authentification
if st.session_state["authentication_status"]:
    # L'utilisateur est authentifié
    MENU_KEY="main_menu"
    with st.sidebar:
        # Bouton de déconnexion dans la barre latérale
        authenticator.logout("Déconnexion", "main")
        st.write(f'Bienvenue *{st.session_state["name"]}*')

        # Menu de navigation dans la barre latérale
        selected = option_menu(
            menu_title=None,  # Pas de titre pour le menu
            options=["Accueil", "Photos de mon chat"], # Options du menu
            menu_icon="cast", # Icône optionnelle pour le menu lui-même
            default_index=0, # Élément sélectionné par défaut
            key=MENU_KEY,
        )

    # Affichage du contenu de la page sélectionnée

    if selected == "Accueil":
        accueil()
    elif selected == "Photos de mon chat":
        chat()

        

elif st.session_state["authentication_status"] is False:
    # L'authentification a échoué
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    # Aucune tentative de connexion ou champs vides
    st.warning('Les champs username et mot de passe doivent être remplis')
