# Quelques bonnes pratiques génériques pour les données numériques en sciences sociales

## Objectifs


*Contexte* : alors que le format numérique des données s'impose, la période est au renforcement des préconisation sur le rapport aux données dans la recherche (ex. principes FAIR) pour favoriser la collaboration et le partage.

*Question* : quelles sont les bonnes pratiques générales à recommander sur la collecte et le traitement des données dans l'enseignement de l'enquête en sciences sociales qui soient le plus possibles agnostiques par rapport aux méthodes utilisées ?

*Problèmes* : 

(1) il existe une diversité de méthodes en sciences sociales allant de l'observation aux approches computationnelles ; 
(2) le formalisme et la complexité de certaines règles formulées pour la science ouverte les rend difficilement utilisables pour des enquêtes par des étudiants ;

*Objectif* : construire une fiche destinée à un enseignement de sciences sociales sur la réflexion autour des données afin de favoriser leur constitution et leur usage efficace dans un cadre collaboratif où le type de données utilisées n'est pas défini a priori et peut éventuellement évoluer.

- limiter les problèmes pendant l'enquête
- faciliter la collaboration
- favoriser la reproductibilité
- augmenter la pérénnité

*Quelques exemples pratiques* :

- une étudiante en anthropologie conduisant principalement son enquête par observations utilisant principalement un journal de terrain mais qui à terme va devoir coder ses observations
- un géographe social recourant à la fois à des données spatiales et à la conduite d'entretiens qui va utiliser à la fin QGIS pour une carte
- un groupe d'étudiant en sociologie devant faire passer une enquête par questionnaire en ligne

*Choix* :

- Un ordre "chronologique" suivant les temps de l'enquête
- Ne pas rentrer en détail dans les aspects spécifiques de chaque méthode (littérature dédiée à chaque fois)
- Lister une série de recommandations mais aussi des questions ouvertes pour favoriser la réflexivité

*Remarques* :

- beaucoup de conseil sur les données existent du point de vue de programmeurs
- trouver un équilibre entre une standardisation complète (par exemple des métadata https://ddialliance.org/) et une idiosyncrasie des pratiques

## Recommandations

### 1. Préparer

- **Avoir une conception ouverte de ce qui peut constituer une donnée utile**

Penser à explorer les ensembles de données déjà collectées disponibles. Certaines données ne deviennent utiles qu'à partir du moment où elles sont mises en relation avec d'autres. Ou qu'elles soient l'objet d'un travail de codage, par exemple collecter des images pour ensuite les décrire. Bien s'assurer de l'adéquation des données envisagées avec la méthodologie et la question. Par exemple : l'observation est toujours préférable à l'entretien pour documenter une pratique, mais se trouve plus coûteux à organiser ; le contenu d'un propos tenu sur les réseaux sociaux ne vous renseignera que peu sur les propriétés de son émetteur.

- **Anticiper les conséquences possibles des données une fois collectées**

Collecter et rassembler des données ouvre de nouvelles possibilités. Se poser la question du caractère légal et éthique des informations collectées : est-ce que la collecte peut se faire dans le respect de la loi et des règlement concernés par le domaine ? est-ce que cela va avoir des conséquences sur des personnes concernées ? Suivant le type d'enquête, certaines contraintes spécifiques se posent (par exemple sur les données de santé)

- **Envisager la dimension matérielle des données**

La question se pose du statut concret de ces données, comment elles se présentent, sous quel format et quelle taille vont-elles avoir. Cela doit amener à se poser différentes questions : quel support concret va être utilisé pour collecter les données ? Est-ce que l'accès est possible ? Est-ce qu'il est possible de faire un test pour voir s'il n'y a pas de souci ? Quel est le meilleur équipement disponible pour la tâche ? Est-ce que l'équipement existe et est fiable ? 

### 2. Collecter

- **Organiser le stockage des données collectées pour favoriser le travail collectif**

Partir du principe qu'il faut pouvoir revenir à ses données même après une période un peu longue. Est-ce que toutes les données sont rassemblées au même endroit ? Comment faire pour limiter la perte d'information ? Qui peut ajouter des éléments ?  Est-ce que tout le monde utilise les mêmes conventions ? Cela passe par rassembler les données au même endroit. Par exemple créer un dossier racine dans lequel se trouvera tous les éléments clairement organisés et nommés. L'arborescence des fichiers est importante pour se retrouver dans des projets collectifs. Ne pas hésiter à construire une hiérarchies de dossiers pour faciliter le classement. Penser aussi à documenter la logique utilisée pour organiser le projet, dans l'idéal avec un document récapitule l'organisation du projet. Pour les dossiers et les fichiers, privilégier des noms courts et signifiants, et éviter des caractères spéciaux dans les noms. Dans le cas où ces données sont partagées sur un cloud, s'assurer qu'il n'y a pas de risque de divulgation de données sensibles, et que tout le monde puisse avoir accès. Penser par exemple que les collaborateurs travaillent peut être sur un autre système d'exploitation.

- **Favoriser des supports de données interopérables faciles à lire par l'humain et par l'ordinateur**

Réfléchir sur les données est une collaboration entre le jugement humain et l'ordinateur. Dans l'idéal, donnez-vous la possibilité de simplifier le travail pour les deux. Cela passe notamment par l'usage de formats libres de fichier facilitant l'interopérabilité. Un format de fichier libre signifie qu'il peut être accessible par une diversité de logiciel. Pour les tableurs, cela signifie un stockage en CSV ou en XLSX. Pour les fichiers textes, le format TXT, et éventuellement DOCX. Pour des données plus complexes, cela peut être par exemple un format JSON qui va cependant être difficile à lire par un humain. Dans tous les cas, évitez si possibles des formats spécifiques à un seul logiciel ou uniquement pour l'humain (par exemple les PDF)

- *Maximiser la modularité*

S'il est possible de ne pas mélanger deux éléments ensemble, s'assurer de le faire. S'il y a plusieurs types de données collectées, les conserver dans des ensembles séparer tout en s'assurant de la possibilité de pouvoir les relier ensemble, par exemple avec un identifiant commun. Dans certains cas, cela peut poser la question de construire un registre (un tableur avec des informations pour chaque donnée collectée) voire une base de données.

- **Etre le plus cohérent possible pendant la collecte de données**

Cela signifie appliquer dans la mesure du possible les mêmes règles dans les étapes. Dans certains cas, par exemple avec des entretiens qui évoluent, la cohérence se fait sur l'ensemble de la démarche (processus). S'il y a un codage qui intervient, s'assurer de la cohérence de ce codage tout du long et entre les différents enquêteurs. Dans un travail collaboratif, prendre le temps en amont de définir ces règles.

- **Documenter au mieux les données en y associant des métadonnées**

Les données collectées sont toujours associées à un contexte, qui est souvent nécessaire pour pouvoir les comprendre et identifier les limites. Il est nécessaire d'associer chaque données à un ensemble d'informations appelées métadonnées qui permettent de décrire les conditions de production et les caractéristiques de ces données. Cela peut prendre par exemple la forme d'un fichier spécifique qui décrit le contenu des données, la date de collecte, la manière dont elles ont été collectées, éventuellement les modifications qui ont été faites.

### 3. Traiter

- **Séparer (le plus possible) la phase de collecte des données (données brutes) de la phase de traitement (données consolidées)**. 

Cela passe par la conservation des données brutes et la description des opérations qui permettent de passer des données brutes aux données traitées. Ces données "nettoyées" (tidy data) servent ensuite de base à l'analyse. Cela vaut la peine de prendre du temps pour faire cette gestion des données.

- **Traiter les données passe par une transformation et un enrichissement des données brutes**

 Cela peut passer soit parune étape de codage, soit par une  transformation, soit par un appariement avec d'autres données. Comme pour la collecte, il est important de maximiser la cohérence des opérations. Ne pas hésiter à constituer des étapes intermédiaires qui permettent de suivre le processus, d'autant qu'il y a souvent un aller-retour avec l'analyse. Comment s'assurer de conserver au maximum les étapes de transformation des données ? Séparer chacune des étapes pour ne pas faire de transformations trop radicales.  Ne pas hésiter à appliquer un principe de réductionnisme : découper une étape en sous-étapes. Par exemple, avec un tableur, cela peut être créer un document différent (ou un onglet) pour chaque étape.

- **Identifier clairement le rôle des logiciels utilisés et les contraintes que cela va avoir sur les données traitées**

 Les traitements sont distincts des données, et se font avec des logiciels. Certains logiciels propriétaires exercent une logique d'emprise sur vos données et les capture en réalisant certaines opérations que d'autres ne font pas (ou pas de la même manière) et en ne permettant pas facilement de faire ressortir vos données. Par ailleurs ils peuvent être couteux. Le fait de privilégier les logiciels libres permet souvent d'éviter ces deux problèmes, permettant aussi généralement l'intercompatibilité. Une bonne manière de procéder est de réfléchir à deux manières différentes de faire le même traitement pour être sûr de ne pas être bloqué. Dans le cas des logiciels comme services en ligne (Software as a service), vérifiez ce que le prestataire fait de vos données, et si vous n'allez pas vous retrouver limité par les options offertes. Par exemple, pour passer un questionnaire, préférez une implémentation d'un logiciel libre comme Limesurvey dans votre université plutôt que de passer par un Google Form.

- **Formaliser et automatiser (le plus possible) les traitements réalisés sur les données brutes pour limiter les opérations "à la main"**

 Identifier les différentes étapes réalisées. A minima cela passe par la création d'un journal de traitement qui décrit les opérations réalisées sur les données brutes pour produire les données traitées. A maxima, cela se réalise avec des scripts (open refine, R, Python, macros, etc.). Cela permettra non seulement aux collaborateurs de suivre les traitements réalisés mais aussi d'assurer une forme de reproductibilité. Il est aussi important de limiter les modifications à la main difficiles à automatiser : par exemple, si vous codez dans un tableau une information, il est préférable de créer une nouvelle colonne avec un code explicite que d'utiliser un code couleur plus difficile à extraire pour un ordinateur. Cela peut aussi passer par la création de listes de code ou de recodage pour permettre leur systématisation (codebook ou script).

- **Tester la cohérence des données et des traitements**

Les opérations de traitement rencontrent souvent des cas particuliers qui n'ont pas été prévus. Ou donnent des résultats inattendus dans certains cas. Surtout quand il y a une série de traitements qui s'enchaînent, il faut prendre le temps de vérifier qu'on introduit pas une erreur systématique. Dans le cas d'un codage d'entretien c'est par exemple de vérifier la cohérence d'un codage avec le reste du propos. Dans le cas de données tabulaire, c'est de vérifier quelques lignes et de s'assurer qu'il n'y a pas de souci. Faire attention aussi aux valeurs manquantes.

### 4. Analyser

- **Bien identifier l'analyse comme un ensemble d'étapes spécifiques à partir des données.**

Les analyses utilisent les données traitées mises en forme, et représentent le moment de synthèse en vue d'obtenir des résultats. Cela signifie que les analyses doivent être faites en lien avec la problématique générale de l'enquête. Pour cela, il est important de se poser la question si les analyses faites correspondent bien à ce qui est recherché, et si cela permet de répondre aux questions posées. Il n'est pas nécessaire d'être captif d'un unique logiciel pour l'analyse et il est préférable de tester différentes stratégies.

- **Ne pas attendre d'avoir toutes les données pour mettre en place sa stratégie de traitement**

Faire des tests sur les données préalables permet d'identifier des problèmes non identifiées et de donner une idée de la complexité de l'analyse : ambiguité dans les codages, limites des outils disponibles, etc. Avez-vous testé sur quelques éléments les analyses que vous voulez réaliser ?

- **Identifier les différentes versions de l'analyse**

Analyser est souvent un mouvement progressif où les résultats sont produits progressivement en lien avec la réflexion. Comment conserver les différentes versions d'une même analyse ? Comment faire référence à certaines analyses qui sont réalisées dans un autre logiciel ou un autre dossier ? 

- **Référencer les méthodes utilisées**

Il y a toujours plusieurs façons de traiter des données. Il est important de préciser quelle est la démarche générale suivie, surtout pour des traitements qui nécessitent de faire de choix d'interprétation ou des hypothèses. S'il existe des références publiées ou des travaux dont vous suivez l'exemple, penser à les mentionner. C'est d'autant plus important quand il s'agit de traitements statistiques.

### 5. Préserver

- **Versionner et sauvegarder régulièrement les étapes du travail**

Si les solutions cloud permettent souvent une sauvegarde continue des données, ce n'est pas toujours facile de revenir à une version antérieure. C'est aussi le cas quand vous faites circuler un document qui existe donc dans plusieurs versions. Il faut s'assurer d'une logique homogène de nommage des versions (nom_v1, nom_v2, etc. ou avec la date, écrite de manière systématique avec la personne qui a modifié le document). Si vous travaillez sur du code, ou que vous voulez maîtriser vos sauvegardes, vous pouvez vous tourner vers des outils de gestion de version. Pensez à différents moments de votre travail à faire une sauvegarde des documents dans un support stable (clé usb, disque dur sur un autre ordinateur). 

- **Archiver le travail réalisé pour permettre à d'autres (ou à votre moi futur) de revenir dessus**

A la fin d'une phase de travail, prenez le temps de faire un peu de gestion de données pour assurer que toutes les informations soient disponibles pour que quelqu'un puisse reprendre vos données, notamment vous dans un an. Est-ce qu'il n'y a que des éléments pertinents ? Est-ce que j'ai supprimé tous les éléments qui n'ont rien à voir ? Est-ce que les fichiers sont bien nommés et dans un format facile à ouvrir ? Est-ce qu'il y a une synthèse ?


### 6. Partager

- **Rendre disponible des informations utilisables**

Dans certains cas, il est intéressant de partager les données que vous avez collectées ou une partie des analyses. Dans tous les cas, vous devez vous assurer que vous pouvez partager ces données (anonymisation). Mais il est aussi important de penser à la possibilité d'accéder aux informations que vous partagez : est-ce que vos données sont bien décrites dans des métadonnées ? Est-ce que le support sur lequel vous partagez vos donnés ou vos résultats est accessible ? Est-ce que l'entrepot de données choisi est pérenne ? Qui est susceptible d'accéder à vos données ? Est-ce que c'est nécessaire de conserver toutes les données ou une partie suffit ?

- **Penser à la licence des documents**

Suivant ce que vous partagez, pensez à préciser le type de licence - les droits d'utilisation - qui s'appliquent.

## Pour aller plus loin et réfléchir : 

- Broman KW and Woo KH (2018) Data Organization in Spreadsheets. American Statistician 72(1). Taylor & Francis: 2–10. DOI: 10.1080/00031305.2017.1375989.
- Levain A, Revelin F, Beurier A-G, et al. (2023) La crédibilité des matériaux ethnographiques face au mouvement d’ouverture des données de la recherche. Revue d’anthropologie des connaissances 17(2): 1–24. DOI: 10.4000/rac.30291.
- Data Organization in Spreadsheets for Social Scientists de Datacarpentry https://datacarpentry.org/spreadsheets-socialsci/
- Guide de bonnes pratiques sur la gestion des données de la recherche https://mi-gt-donnees.pages.math.unistra.fr/guide/00-introduction.html
- Célya Gruson-Daniel, Groupe Projet Réussir L'Appropriation De La Science Ouverte. Décliner la science ouverte : Rapport final. [Rapport de recherche] Comité pour la science ouverte. 2022, 149 p. ⟨hal-03798504⟩
- Open Science Training Handbook, https://open-science-training-handbook.github.io/Open-Science-TrainingHandbook_FR/
- How to write a data management plan https://libguides.colostate.edu/data-donuts/dmp
