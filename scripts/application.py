import streamlit as st
import pandas as pd
import europresse
from io import StringIO
import matplotlib.pyplot as plt

# Deux parties dans l'application :
# - transformation Europresse -> CSV
# - création d'un graphique

# Transformation Europresse

# Fonction convertissat en format csv et mis en chache
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

st.title('Outil 1 : Transformation Europresse HTML vers CSV')
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

st.markdown("""---""")

st.title("Outil 2 : Création de graphique temporel à partir d'un fichier CSV")
st.write("""Le fichier doit avoir une colonne **Date** avec les dates au format *Année-Mois-Jour* ou *Année* 
         et une colonne **Codage** avec un ou des codes non nuls (code unique = une seule courbe ; 
         plusieurs codes = plusieurs courbes)""")

def tracer_graphique(df,d):
   scale = {"Année":"y","Mois":"m","Jour":"d"}
   df["num"] = 1 # valeur par article pour comptage
   leg = []
   fig,ax=plt.subplots(1,figsize=(10,3))
   for i,j in df.groupby("Codage"):
      leg.append(i)
      j.set_index("Date")["num"].resample(scale[d]).sum().plot(ax=ax,style=".-")
   plt.legend(leg)
   plt.title("Evolution temporelle du corpus")
   plt.xlabel("Temps (par %s)"%scale[d])
   plt.ylabel("Nombre d'articles")
   plt.tight_layout()
   return fig

#  Chargement de données
format_date = st.selectbox("Format de la date",("AAAA-MM-JJ","AAAA"))
d = st.selectbox("Niveau de regroupement",("Année","Mois","Jour"))
csv_file = st.file_uploader("Choisir un fichier CSV", accept_multiple_files=False)
if pd.notnull(csv_file):
   df = pd.read_csv(csv_file)
   try:
      if format_date == "AAAA-MM-JJ":
         df["Date"] = pd.to_datetime(df["Date"])
      if format_date =="AAAA":
         df["Date"] = pd.to_datetime(df["Date"],format="%Y")
   except:
       "La date ne peut pas être convertie"

   if not "Date" in df.columns:
       st.write("Il n'y a pas de champ Date")
   elif not "Codage" in df.columns:
       st.write("Il n'y a pas de champ Codage")
   else:
       fig = tracer_graphique(df,d)
       st.pyplot(fig)
       
   