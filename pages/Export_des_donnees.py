import streamlit as st
import pandas as pd

st.header("📤 Export des données")

if 'df_couche' in st.session_state:
    df_couche = st.session_state.df_couche
    selected_couche = st.session_state.selected_couche

    # Export données filtrées
    csv_data = df_couche.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Télécharger les données filtrées",
        data=csv_data,
        file_name=f"donnees_couche_{selected_couche}.csv",
        mime="text/csv"
    )

    # Calculs Dykstra à exporter aussi
    perm_values = df_couche['perm'].dropna().values
    k50 = pd.Series(perm_values).quantile(0.5)
    k841 = pd.Series(perm_values).quantile(0.841)
    v = (k841 - k50) / k841 if k841 != 0 else float('nan')

    result = pd.DataFrame({
        "Couche": [selected_couche],
        "K50 (mD)": [k50],
        "K84.1 (mD)": [k841],
        "Indice V": [v]
    })

    csv_result = result.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Télécharger les résultats d'analyse",
        data=csv_result,
        file_name=f"resultats_couche_{selected_couche}.csv",
        mime="text/csv"
    )
else:
    st.warning("Aucune donnée à exporter. Veuillez d'abord appliquer les filtres.")
