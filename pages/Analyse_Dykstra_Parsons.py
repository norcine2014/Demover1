import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("📊 Analyse Dykstra-Parsons")

if 'df_couche' in st.session_state:
    df_couche = st.session_state.df_couche
    selected_couche = st.session_state.selected_couche

    perm_values = df_couche['perm'].dropna().values
    perm_sorted = np.sort(perm_values)
    n = len(perm_sorted)
    prob = np.arange(1, n + 1) / (n + 1) * 100

    k50 = np.percentile(perm_values, 50)
    k841 = np.percentile(perm_values, 84.1)
    v = (k841 - k50) / k841 if k841 != 0 else np.nan

    st.markdown(f"""
    ### Résultats pour la couche `{selected_couche}`
    - **K50 (médiane)** : `{k50:.2f}` mD
    - **K84.1** : `{k841:.2f}` mD
    - **Indice V** : `{v:.3f}`
    """)

    # Graphique log-probabilité
    fig, ax = plt.subplots()
    ax.semilogy(prob, perm_sorted, 'o-', color='steelblue', label='Perméabilités')
    ax.axvline(50, color='green', linestyle='--', label='K50')
    ax.axvline(84.1, color='red', linestyle='--', label='K84.1')
    ax.axhline(k50, color='green', linestyle=':')
    ax.axhline(k841, color='red', linestyle=':')
    ax.set_xlabel("Probabilité cumulée (%)")
    ax.set_ylabel("Perméabilité (mD)")
    ax.set_title("Papier log-probabilité")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.legend()
    st.pyplot(fig)

    # Boxplot par puits
    fig2, ax2 = plt.subplots()
    df_couche.boxplot(column='perm', by='puits', ax=ax2, grid=False)
    ax2.set_ylabel("Perméabilité (mD)")
    ax2.set_title("Distribution des perméabilités par puits")
    ax2.figure.suptitle("")
    st.pyplot(fig2)

else:
    st.warning("Veuillez d'abord importer et filtrer les données.")
