
import streamlit as st

# Forcer l'ouverture de la sidebar
st.set_page_config(
    page_title="Hétérogénéité - Dykstra-Parsons",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Optionnel : forcer du contenu dans la sidebar
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    st.info("Utilisez le menu ci-dessus pour changer de page.")

# Corps de la page principale
st.title("🛢️ Analyse de l’hétérogénéité d’un réservoir pétrolier")

st.markdown("""
Bienvenue dans cette application interactive basée sur la méthode **Dykstra-Parsons**.

👉 Utilisez le **menu latéral** pour accéder aux différentes fonctionnalités :

- 📁 **Import et filtres**
- 🗺️ **Carte interactive**
- 📊 **Analyse Dykstra-Parsons**
- 📤 **Export des données**

---

ℹ️ Cette  application vous permet :
- De charger vos fichiers CSV contenant les données de perméabilité.
- De filtrer par couche, puits et valeurs de perméabilité.
- D’afficher les points sur une carte.
- De générer automatiquement les graphiques d’analyse.
- D’exporter les résultats.
""")

