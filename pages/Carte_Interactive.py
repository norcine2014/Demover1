import streamlit as st
import pydeck as pdk

st.header("🗺️ Carte interactive des points de mesure")

if 'df_couche' in st.session_state:
    df_couche = st.session_state.df_couche

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=df_couche['latitude'].mean(),
            longitude=df_couche['longitude'].mean(),
            zoom=8,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_couche,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
else:
    st.warning("Veuillez d'abord importer et filtrer les données dans la page d'accueil.")
