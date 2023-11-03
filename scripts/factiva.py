import pandas as pd
import bs4 as bs
import regex as re
import datetime
from zipfile import ZipFile
from europresse import reco_date

__version__ = "0.0.1"

"""
Attention ce script est en version beta : vérifiez vos données
"""

def extract(html): 
    """
    Extraction de données d'une page html factiva (nombre limités de champs)
    """
    corpus_html = bs.BeautifulSoup(html,"lxml") 
    
    # deux balises qui se contiennent, ne garder que celle de plus haut niveau
    # + ajouter le dernier article qui a une balise spécifique
    corpus_html = [i for i in corpus_html.find_all("div",{"class":"article"}) if i.find("div",{"class":"article"})]\
                + corpus_html.find_all("div",{"class":"lastarticle"}) 
    # boucle sur les articles
    
    if len(corpus_html)<1:
        print("Problème dans l'extraction des données")
        return None
    
    corpus_csv = []
    for frag in corpus_html:
        try:
            titre = frag.find("span").text
        except:
            titre = None
        try:
            texte = " ".join([i.text for i in frag.find_all("p",{"class":"articleParagraph"})])
        except:
            texte = None
        try:
            date,journal = re.findall("mots</div><div>(.*?)</div><.*?>(.*?)<",str(frag.contents).replace("\n",""))[0]
            if len(journal)==5 and ":" in journal: # cas où c'est l'heure qui a été prise en compte
                journal = frag.find_all("span",{"class":"colorLinks"})[0].text

        except:
            date,journal = None,None
        # ajouter un champ brut dans le cas où le nom du journal est mal codé
        try:
            chapeau_brut = re.findall("mots</div><div>(.*?)<p>",str(frag.contents).replace("\n",""))[0]
            nettoyer = ['<span class="colorLinks">','<div>',"</div>",'</span>']
            for k in nettoyer:
                chapeau_brut = chapeau_brut.replace(k," ")
        except:
            chapeau_brut = None

        corpus_csv.append([titre,date,journal,chapeau_brut,texte])
    return corpus_csv

def get_table(data):
    """
    Mise en forme du tableau factiva
    """
    if data==None:
        print("Erreur dans la conversion du tableau")
        return None
    
    table = pd.DataFrame(data,columns=["Titre_raw","Date_raw","Journal_raw","Chapeau_raw","Texte_raw"])
    table["Date_mod"] = table["Date_raw"].apply(reco_date)
    return table