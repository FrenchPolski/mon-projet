import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Portefeuille Bitcoin",
    layout="centered",
)

# Bannière d'accueil
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #f39c12;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 18px;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 30px;
    }
    .cta-button:hover {
        background-color: #d35400;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titres
st.markdown('<h1 class="main-title">Bienvenue sur votre Portefeuille Bitcoin</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">Gérez vos actifs numériques en toute simplicité et sécurité.</h3>', unsafe_allow_html=True)

# Section "Aperçu du portefeuille"
st.markdown('<div class="info-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Solde BTC", value="0.245 BTC", delta="↗ +0.005 BTC")
    st.metric(label="Équivalent en USD", value="$9,870", delta="↗ +$210")

with col2:
    st.image(
        "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
        caption="Bitcoin",
        width=150,
    )

st.markdown('</div>', unsafe_allow_html=True)



# Pied de page
st.markdown("---")
st.markdown(
    """
    <p style="text-align:center; color:#7f8c8d; font-size:14px;">
    © 2024 Portefeuille Bitcoin Datavisualisation Pierre PORTE & Nolwenn GAUTIER. Tous droits réservés. <br>
    Vos actifs numériques en toute sécurité.
    </p>
    """,
    unsafe_allow_html=True,
)
