import streamlit as st
import pandas as pd

st.header("📁 Importer les données et appliquer des filtres")

# Chargement CSV
df = None
if 'df' not in st.session_state:
    uploaded_file = st.file_uploader("Importer un fichier CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
else:
    df = st.session_state.df

if df is not None:
    required_cols = {'puits', 'couche', 'perm', 'latitude', 'longitude'}
    if not required_cols.issubset(df.columns):
        st.error(f"Le fichier doit contenir les colonnes : {', '.join(required_cols)}")
    else:
        st.success("Données chargées avec succès")
        st.dataframe(df.head())

        # Filtres interactifs
        selected_puits = st.multiselect("Filtrer par puits", df['puits'].unique(), default=df['puits'].unique())
        min_perm, max_perm = st.slider("Plage de perméabilité (mD)", float(df['perm'].min()), float(df['perm'].max()), (float(df['perm'].min()), float(df['perm'].max())))
        selected_couche = st.selectbox("Sélectionner une couche", sorted(df['couche'].unique()))

        df_filtered = df[(df['puits'].isin(selected_puits)) & (df['perm'].between(min_perm, max_perm))]
        df_couche = df_filtered[df_filtered['couche'] == selected_couche]

        st.session_state.df_filtered = df_filtered
        st.session_state.df_couche = df_couche
        st.session_state.selected_couche = selected_couche

        st.markdown(f"### Aperçu des données filtrées pour la couche `{selected_couche}`")
        st.dataframe(df_couche)
else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
