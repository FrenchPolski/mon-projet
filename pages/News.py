import streamlit as st
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd
import requests

# Simuler des données de performance
dates = pd.date_range(start="2023-01-01", end=datetime.now(), freq="M")
prices = [20000 + i * 1000 + (i ** 1.5) * 500 for i in range(len(dates))]

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines+markers', name="Prix BTC"))
fig.update_layout(title="Tendance du Prix de Bitcoin", xaxis_title="Date", yaxis_title="Prix en USD")

st.plotly_chart(fig, use_container_width=True)

# Titre de la page
st.title("Dernières Actualités sur le Bitcoin")
st.markdown("")

# Fonction pour récupérer les nouvelles
def fetch_bitcoin_news(api_key, max_articles=2):
    url = f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&language=fr&pageSize={max_articles}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        st.error("Erreur lors de la récupération des nouvelles. Vérifiez votre clé API.")
        return []

# Remplacez "VOTRE_CLE_API" par votre clé NewsAPI
API_KEY = "6539bf5d9bd34ffca2d0f0ab4870d763"

# Récupérer les articles
articles = fetch_bitcoin_news(API_KEY)

# Afficher les articles
if articles:
    for article in articles:
        # Titre
        st.subheader(article["title"])
        
        # Image
        if article["urlToImage"]:
            st.image(article["urlToImage"], use_column_width=True)
        else:
            st.write("📷 Image non disponible")

        # Description
        st.write(article["description"] or "Aucune description disponible.")
        
        # Lien vers l'article complet
        st.markdown(f"[Lire l'article complet]({article['url']})", unsafe_allow_html=True)
        
        # Séparation entre les articles
        st.markdown("---")
else:
    st.write("Aucune actualité disponible pour le moment.")

