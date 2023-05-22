
import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import plotly.express as px
from pandas.plotting import scatter_matrix

# Titre de l'application
st.title('Analyse des actions')



# Sélection des dates
start = st.date_input('Date de début', datetime.datetime(1985, 1, 1))
end = st.date_input('Date de fin', datetime.datetime.now())

# Téléchargement des données
pepsi = yf.download('PEP', start=start, end=end)
coca = yf.download('KO', start=start, end=end)

# Graphique des prix d'ouverture
st.subheader('Prix d\'ouverture')
plt.figure(figsize=(16, 8))
pepsi['Open'].plot(label='Pepsi')
coca['Open'].plot(label='Coca')
plt.title('Open Price')
plt.legend()
st.pyplot(plt.gcf())

print(coca['Volume'].idxmax())


# Graphique du volume
st.subheader('Volume')
plt.figure(figsize=(16, 8))
coca['Volume'].plot(label='Coca')
pepsi['Volume'].plot(label='Pepsi')
plt.title('Volume')
plt.legend()
st.pyplot(plt.gcf())

st.subheader('matrice de dispersion')
com = pd.concat([pepsi['Open'], coca['Open']], axis=1)
com.columns = ['Pepsi', 'Coca']
scatter_matrix(com, figsize=(8, 8))
st.pyplot(plt.gcf())


df = pd.read_csv("pep-co(1).csv")
df[['prix coca pepsi', 'Pays']] = df['Colonne1;Colonne2'].str.split(';', expand=True)
st.write(df)
st.title('Analyse des prix de coca et pepsi par pays')
fig = px.choropleth(
    data_frame=df,
    locations='prix coca pepsi',
    locationmode='country names',
    color='Pays',
    color_continuous_scale='YlOrRd',
    title='Analyse des données quantitatives par pays'
)
st.plotly_chart(fig, use_container_width=True)

pepsi['Returns'] = pepsi['Close'].pct_change(1)
coca['Returns'] = coca['Close'].pct_change(1)

st.subheader('Histogramme des rendements')
fig, ax = plt.subplots(figsize=(10, 8))

coca['Returns'].hist(bins=100, label='Coca', figsize = (10,8) ,alpha=0.6,ax=ax)
pepsi['Returns'].hist(bins=100, label='Pepsi', alpha = 0.9,ax=ax)
plt.legend()
plt.show()
st.pyplot(fig)

st.title('Evolution du taux d\'obéseité en France, au mexique et aux US de 2000 à 2012')
st.image('image.png')
