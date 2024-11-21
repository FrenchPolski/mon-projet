import streamlit as st
import requests
import pandas as pd
import time
import csv

st.title("My BTC Wallet")



money_df = pd.read_csv('money.csv')
derniere_valeur_argent = money_df.iloc[-1, -1]
money = derniere_valeur_argent

possessbtc=pd.read_csv('numberbtc.csv')
btc2=possessbtc.iloc[-1, -1]

var=pd.read_csv('var.csv')
var2=var.iloc[-1, -1]

st.write('Argent disponible : ', money, "€")
st.write("Nombre de BTC possédé : ", btc2, "BTC")
st.write("Variation Portefeuille : ",money-var2, "€")

url_root = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url_root)


if response.status_code == 200:
    data = response.json()  
    

    df = pd.DataFrame(data['bpi']).T 

    st.write(df)

    bitcoin_usd = data['bpi']['EUR']['rate_float']
    

else:
    st.error(f"Erreur : {response.status_code}")


st.title("   ")
btc = pd.read_csv("/Users/pierreporte/Documents/Université/Master/M2/Semestre 1/Data/Analyse Python/StreamLit/Données API/projet/prix_bitcoin.csv")
 



##  ACHAT

if st.button("Achat 1 BTC"):
    if money>bitcoin_usd:
        df = pd.DataFrame({btc2+1
         })
        
        df.to_csv('numberbtc.csv', index=False, mode='a', header=not pd.io.common.file_exists('numberbtc.csv'))
        df = pd.DataFrame({money-bitcoin_usd
         })
        
        df.to_csv('money.csv', index=False, mode='a', header=not pd.io.common.file_exists('money.csv'))
        df = pd.DataFrame({
                'Date': [data['time']['updated']],
                'Prix_Bitcoin_USD': [bitcoin_usd]
         })
        
        df.to_csv('prix_bitcoin.csv', index=False, mode='a', header=not pd.io.common.file_exists('prix_bitcoin.csv'))

st.write(btc)




##VENTE


if st.button("Vente 1 BTC"):
    if btc2>=1:

        df = pd.DataFrame({btc2-1
            })
            
        df.to_csv('numberbtc.csv', index=False, mode='a', header=not pd.io.common.file_exists('numberbtc.csv'))
        df = pd.DataFrame({money+bitcoin_usd
            })
            
        df.to_csv('money.csv', index=False, mode='a', header=not pd.io.common.file_exists('money.csv'))
        df = pd.DataFrame({
                'Date': [data['time']['updated']],
                'Prix_Bitcoin_USD': [bitcoin_usd]
            })

        df.to_csv('ventebtc.csv', index=False, mode='a', header=not pd.io.common.file_exists('ventebtc.csv'))
   

vente = pd.read_csv("/Users/pierreporte/Documents/Université/Master/M2/Semestre 1/Data/Analyse Python/StreamLit/Données API/projet/ventebtc.csv")

st.write(vente)




##################




if st.checkbox("Lancement temps réel"):
    while True:
    
        # Afficher la date et l'heure actuelle
        st.write("Heure actuelle :", time.strftime("%H:%M:%S"))
        
        # Faire une pause pour éviter de surcharger l'interface
        time.sleep(0.5)
        
        # Redémarrer le script
        st.experimental_rerun()


