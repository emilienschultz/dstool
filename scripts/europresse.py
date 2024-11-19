import datetime
from zipfile import ZipFile

import bs4 as bs
import pandas as pd
import regex as re

__version__ = "0.1.1"

"""
Attention ce script est en version beta : vérifiez vos données
"""


def extract(html):
    """
    Extraction de données d'une page Europesse (nombre limités de champs)
    """
    corpus_html = bs.BeautifulSoup(html, "lxml")
    corpus = []  # tableau que l'on va remplir avec les données
    for i in corpus_html.find_all("article"):
        # on regarde s'il y a un titre dans l'article
        try:
            titre = i.find("div", {"class": "titreArticle"}).text
        except:
            titre = None  # sinon on renvoie rien

        # Pareil pour la date/header
        try:
            header = i.find("span", {"class": "DocHeader"}).text
        except:
            header = None

        # Le nom de la publicatoin
        try:
            publication = i.find("span", {"class": "DocPublicationName"}).text
        except:
            publication = None

        # le contenu
        try:
            text = i.find("div", {"class": "DocText clearfix"}).text
        except:
            text = None

        # le contenu
        try:
            auteur = i.find("div", {"class": "docAuthors"}).text
        except:
            auteur = None

        # On ajoute ces éléments au corpus
        corpus.append([header, titre, publication, text, auteur])

    return corpus  # On renvoie les informations


def reco_date(x):
    """
    Recoder la date telle que présente dans un fichier europresse
    """
    mois = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12",
    }

    try:
        t = re.findall("\d{1,2} \w+ \d{4}", x)
    except:
        t = []

    if len(t) < 1:
        return None

    t = t[0]

    for i in mois:
        if i in t:
            t = t.replace(i, "/%s/" % mois[i]).replace(" ", "")

    try:
        t = datetime.datetime.strptime(t, "%d/%m/%Y")
    except:
        t = None

    return t


def recode_journal(j):
    """
    Recoder le journal
    """
    if pd.isnull(j):
        return None
    r = j.strip().split(",")[0]
    dic = {
        "Ouest-France": "Ouest-France",
        "Le Monde": "Le Monde",
        "Le Figaro": "Le Figaro",
        "Le Progrès": "Le Progrès",
        "L'Est Républicain": "L'Est Républicain",
        "La Voix du Nord": "La Voix du Nord",
        "La Croix": "La Croix",
        "Le Parisien": "Le Parisien",
        "Paris-Normandie": "Paris-Normandie",
        "Le Télégramme": "Le Telegramme",
        "Libération": "Libération",
        "La Nouvelle République du Centre-Ouest": "La Nouvelle République du Centre-Ouest",
        "La République des Pyrénées": "La République des Pyrénées",
        "AFP": "AFP",
        "Sud Ouest": "Sud Ouest",
        "Le Bien Public": "Le Bien Public",
    }
    for i in dic:
        if i in r:
            return dic[i]
    return r


def get_table(data):
    """
    Mise en forme du tableau
    """
    if data == None:
        print("Erreur dans la conversion du tableau")
        return None

    table = pd.DataFrame(
        data,
        columns=["Date_raw", "Titre_raw", "Journal_raw", "Contenu_raw", "Auteur_raw"],
    )
    table["Date_mod"] = table["Date_raw"].apply(reco_date)
    table["Titre_mod"] = table["Titre_raw"].str.strip()
    table["Contenu_mod"] = table["Contenu_raw"].str.strip()
    table["Journal_mod"] = table["Journal_raw"].apply(recode_journal)
    return table
