import streamlit as st

st.set_page_config(page_title="Analyse Dykstra-Parsons", layout="wide")

# Titre principal
st.title("🛢️ Application d’analyse de l’hétérogénéité d’un réservoir pétrolier")

# Menu de navigation avec des boutons
st.markdown("## 🧭 Menu de navigation")
page = st.radio("Choisissez une section :", [
    "🏠 Accueil",
    "📁 Import et Filtres",
    "🗺️ Carte interactive",
    "📊 Analyse Dykstra-Parsons",
    "📤 Export des données"
], horizontal=True)

st.divider()

# Contenu selon la sélection
if page == "🏠 Accueil":
    st.markdown("""
    Bienvenue dans cette application interactive basée sur la méthode **Dykstra-Parsons**.

    👉 Cette application vous permet :
    - D'importer vos données de perméabilité (CSV)
    - De filtrer par couche ou puits
    - De visualiser les données sur une carte interactive
    - D’analyser l’hétérogénéité par log-probabilité
    - D’exporter vos résultats

    Utilisez le menu ci-dessus pour naviguer entre les sections.
    """)

elif page == "📁 Import et Filtres":
    st.subheader("📁 Import de données et filtres")
    st.write("Ici, vous pourrez importer vos fichiers CSV et filtrer les données.")
    # Code d'import et de filtre ici

elif page == "🗺️ Carte interactive":
    st.subheader("🗺️ Carte interactive")
    st.write("Affichage des points géographiques des puits.")
    # Code de carte ici

elif page == "📊 Analyse Dykstra-Parsons":
    st.subheader("📊 Analyse Dykstra-Parsons")
    st.write("Analyse des distributions et log-probabilité.")
    # Code d'analyse ici

elif page == "📤 Export des données":
    st.subheader("📤 Export des données")
    st.write("Téléchargez vos résultats filtrés ou analysés.")
    # Code d'export ici
