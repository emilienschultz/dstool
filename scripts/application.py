import streamlit as st
import pandas as pd
import europresse
from io import StringIO

# Fonction convertissat en format csv et mis en chache
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

st.title('Transformation des fichiers europresse HTML > CSV')
st.write("Les fichiers doivent être en HTML dans le format de sortie d'Europresse/version classique")
st.write("Le traitement utilise BeautifulSoup / Pandas / Streamlit")

#  Chargement de données multiples
uploaded_files = st.file_uploader("Choisir un/des fichiers HTML Europesse", accept_multiple_files=True)

corpus = []

if len(uploaded_files)>0:
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        corpus += europresse.extract(uploaded_file)

    st.write("Taille du corpus %d"%len(corpus))
    df = europresse.get_table(corpus)
    csv = convert_df(df)
    st.download_button(
       "Télécharger le tableau en csv",
       csv,
       "tableau.csv",
       "text/csv",
       key='download-csv'
    )