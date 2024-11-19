import io
import re

import europresse
import factiva
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Trois parties dans l'application :
# - transformation Europresse -> CSV
# - création d'un graphique
# - transformation d'un corpus de textes en phrases contenant une regex


# Fonction convertissat en format
@st.cache_data
def convert_df(df, format="xlsx"):
    if format == "xlsx":
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        return output
    if format == "csv":
        return df.to_csv(index=False).encode("utf-8")
    return None


st.title("DSTool - Outils pour l'annotation de corpus de presse")

st.write("La démarche prévue est la suivante")
st.markdown("""
            - Convertir un corpus HTML > XLSX
            - Découper les textes en éléments contenant certains mots-clés
            - Faire une courbe sur les codage
            """)

st.subheader("Outil 1 : Convertir Europresse/Factiva HTML > XLSX")
st.write(
    "Les fichiers doivent être en HTML dans le format de sortie d'Europresse/version classique ou Factiva"
)
st.write(
    "*Attention : Attention de bien sélectionner soit Europresse soit Factiva en fonction des sources. Certaines sources non journalistiques comme Agrobusiness report ne sont pas très bien parsées (champs nuls dans le tableau final)*"
)

source = st.selectbox("Source des données", ("europresse", "factiva"))
#  Chargement de données multiples
uploaded_files = st.file_uploader(
    "Choisir un/des fichiers HTML Europesse", accept_multiple_files=True
)

corpus = []

if len(uploaded_files) > 0:
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        if source == "europresse":
            corpus += europresse.extract(uploaded_file)
            st.write("Taille du corpus %d" % len(corpus))
            df = europresse.get_table(corpus)
        if source == "factiva":
            corpus += factiva.extract(uploaded_file)
            st.write("Taille du corpus %d" % len(corpus))
            df = factiva.get_table(corpus)

    data = convert_df(df, format="xlsx")
    st.download_button(
        "Télécharger le tableau en xlsx",
        data,
        f"{uploaded_file.name.replace('.html','').replace('.HTML','')}.xlsx",
        "text/csv",
        key="download-file1",
    )

st.markdown("""---""")


st.subheader(
    "Outil 2 : Extraire les phrases d'un corpus de texte contenant des mots (.xlsx)"
)
st.write(
    """Le filtre est une expression régulière (regex). La coupure entre les phrases se fait sur les point (., !, ?) et les retours à la ligne
    
    """
)


def extract_sentences(text, num_phrases, regex):
    """
    Extract sentences from a text with a regex and the frame context
    """
    text = text.replace(". ", "\n")
    text = text.replace("?", "\n")
    text = text.replace("!", "\n")
    sentences = text.split("\n")
    sentences = [
        "\n".join(
            sentences[max(i - num_phrases, 0) : min(i + num_phrases, len(sentences))]
        )
        for i in range(0, len(sentences))
        if re.search(regex, sentences[i])
    ]
    return sentences


# upload the file
file = st.file_uploader(
    "Choisir un fichier .xlsx", accept_multiple_files=False, key="outil3"
)
# if file
if pd.notnull(file):
    df = pd.read_excel(file)
    col_text = st.selectbox("Colonne textes", df.columns)
    val_regex = st.text_input("Saisir une expression régulière", value="vélo")
    num_phrases = st.number_input("Nombre de phrases avant/après", value=1)

    if st.button("Validate"):
        if col_text in df.columns:
            df = df.dropna(subset=[col_text])
            df["explode_sentences"] = df[col_text].apply(
                lambda x: extract_sentences(x, num_phrases, val_regex)
            )
            df = df.explode("explode_sentences")
            df = df[df["explode_sentences"].str.contains(val_regex).fillna(False)]
            df.rename(
                columns={"explode_sentences": f"phrases_{2*num_phrases+1}"},
                inplace=True,
            )
            data = convert_df(df, format="xlsx")
            st.write("Le fichier contient %s lignes qui valident la regex" % len(df))
            st.download_button(
                "Télécharger le tableau en xlsx",
                data,
                f"exploded_{file.name}",
                "text/csv",
                key="download-file2",
            )


st.subheader("Outil 3 : Création de graphique temporel à partir d'un fichier XLSX")
st.write("""Le fichier doit avoir une colonne **Date** avec les dates au format *Année-Mois-Jour* ou *Année* 
         et une colonne **Codage** avec un ou des codes non nuls (code unique = une seule courbe ; 
         plusieurs codes = plusieurs courbes)""")


def tracer_graphique(df, d):
    scale = {"Année": "y", "Mois": "m", "Jour": "d"}
    df["num"] = 1  # valeur par article pour comptage
    leg = []
    fig, ax = plt.subplots(1, figsize=(10, 3))
    for i, j in df.groupby("Codage"):
        leg.append(i)
        j.set_index("Date")["num"].resample(scale[d]).sum().plot(ax=ax, style=".-")
    plt.legend(leg)
    plt.title("Evolution temporelle du corpus")
    plt.xlabel("Temps (par %s)" % scale[d])
    plt.ylabel("Nombre d'articles")
    plt.tight_layout()
    return fig


#  Chargement de données
file = st.file_uploader("Choisir un fichier .xlsx", accept_multiple_files=False)
if pd.notnull(file):
    df = pd.read_excel(file)
    col_date = st.selectbox("Colonne Date", df.columns)
    col_codage = st.selectbox("Colonne Codage", df.columns)
    format_date = st.selectbox(
        "Format de la date", ("AAAA-MM-JJ", "AAAA", "JJ/MM/AAAA")
    )
    d = st.selectbox("Niveau de regroupement", ("Année", "Mois", "Jour"))

    try:
        if format_date == "AAAA-MM-JJ":
            df["Date"] = pd.to_datetime(df[col_date])
        if format_date == "AAAA":
            df["Date"] = pd.to_datetime(df[col_date], format="%Y")
        if format_date == "JJ/MM/AAAA":
            df["Date"] = pd.to_datetime(df[col_date], format="%d/%m/%Y")
    except ValueError:
        "La date ne peut pas être convertie"

    if col_codage in df.columns:
        df["Codage"] = df[col_codage].astype(str)

    if "Date" not in df.columns:
        st.write("Il n'y a pas de champ Date")
    elif "Codage" not in df.columns:
        st.write("Il n'y a pas de champ Codage")
    else:
        fig = tracer_graphique(df, d)
        st.pyplot(fig)

st.markdown("""---""")
st.write("Le traitement utilise BeautifulSoup / Pandas / Streamlit")
st.markdown(
    "Pour tout problème, merci d'ouvrir une issue https://github.com/emilienschultz/dstool/issues"
)
