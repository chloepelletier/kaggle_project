import pandas as pd
import numpy as np
import sklearn as skl
from datetime import datetime

from matplotlib import pyplot as ppl

import src.data.getDataFrames


# PANDA TUTO

# Lire un fichier csv en data frame: (on peut changer les noms de colonnes + le type des colonnes)
pd.read_csv('data/raw/weather_dwd_train_set.csv', sep=';')
# Connaitre les 5 premieres rows:
netteBad.head()
# Connaitre les 5 dernieres rows:
netteBad.tail()
# Connaitre le nombre de colonnes et lignes:
netteBad.shape
# Stat basique, moyenne, std, min, etc sur chaque colonnes / Serie:
netteBad.describe()
netteBad.visitors_pool_total.describe()
# compter les itérations des valeurs dans Series
netteBad.visitors_pool_total.value_counts()
netteBad.visitors_pool_total.value_counts().head()
netteBad.visitors_pool_total.value_counts(normalize=True) * 100
# Utilisation du unique
visitorsUnique = netteBad.visitors_pool_total.unique()
# Type de chaque colonnes:
netteBad.dtypes
# Changer le type d'une colonne
netteBad.visitors_pool_total = netteBad.visitors_pool_total.astype(float)
# Récupérer que les noms de colonnes:
netteBad.columns
# Renommer les colonnes :
netteBad.rename(columns={'visitors_pool_total': 'Visitors', ...}, inplace=True)
netteBad.columns = ['date', 'Visitor', ...]
# Supprimer une colonne:
netteBad.drop('freizeitbad_closed', axis=1, inplace=True)
netteBad.drop(['freizeitbad_closed', 'date'], axis=1, inplace=True)
# Supprimer des row par ID:
netteBad.drop([0, 2], axis=0, inplace=True)
# Trier per colonne dans l'ordre decroissant:
netteBad.sort_values('visitors_pool_total', ascending=False) 
netteBad.sort_values(['visitors_pool_total', 'date']) 
# Selectionner des colonnes précises:
netteBadDate = netteBad.date
netteBadDateAndVisitors = netteBad.date + netteBad.visitors_pool_total # should work but not here
netteBadDateAndVisitors = netteBad[['date', 'visitors_pool_total']]
# Creer une nouvelle colonne
netteBad['date 2'] = netteBad.date
# Faire un filter sur une colonne:
netteBadWith1482Or23Visitors = netteBad[netteBad['visitors_pool_total'].isin(['1482', '23'])]
netteBadWithMoreThan482Visitors = netteBad[netteBad.visitors_pool_total >= 482]
netteBadWithVisitors123 = netteBad[netteBad.visitors_pool_total.astype(str).str.contains('123')]
# Utiliser plusieurs filtres:
netteBadWithMoreThan482VisitorsAndEvent = netteBad[(netteBad.visitors_pool_total >= 1182) & (netteBad.event == 1)]
netteBadWithMoreThan482VisitorsAndEvent = netteBad[(netteBad.visitors_pool_total >= 482) | (netteBad.event == 1)]
# Faire un filter et ne selectionner que certaines colonnes:
visitorWithMoreThan482Visitors = netteBad[netteBad.visitors_pool_total >= 482].visitors_pool_total
visitorWithMoreThan482Visitors = netteBad.loc[netteBad.visitors_pool_total >= 482, 'visitors_pool_total']
visitorWithMoreThan482Visitors = netteBad.loc[netteBad.visitors_pool_total >= 482, ['visitors_pool_total', 'date']]
# Remplacer des valeurs par d'autres
visitorUN = netteBad.visitors_pool_total.astype(str).str.replace('1', 'UN')
# Utiliser un groupBy
netteBad.groupby('bank_holiday').visitors_pool_total.mean() #.plot(kind='bar')
# Obtenir une matrice liant deux colonnes
pd.crosstab(netteBad.visitors_pool_total, netteBad.school_holiday)
# Merger des df ensembles: (fusionne les colonnes totalement identiques, garde des colonnes avec Nan des deux sens)
result = netteBad.append(weather_dwd)
result = netteBad.append([weather_dwd, weather_osnabrueck])
pd.merge(netteBad, weather, on='date', how='outer')
# Connaitre le nombre de valeurs manquantes dans colonnes:
netteBad.isnull().sum()
# Supprimer les rows où au moins une colonne est à NA / toutes à NA:
netteBad.dropna(how='any')
netteBad.dropna(how='all')
netteBad.dropna(subset=['date', 'visitors_pool_total'], how='any')
netteBad.dropna(subset=['date', 'visitors_pool_total'], how='all')
# Remplacer les NA par autre chose
netteBad.fillna(value="pas de valeur", inplace=True)
# Appliquer une fonction basique + lambda sur une colonne
netteBad.visitors_pool_total.astype(str).apply(len)
netteBad.price_adult_max.astype(str).str.split('.').apply(lambda x: x[0])
# Appliquer une fonction personnalisé sur une colonne (récupère le *position* element de chaque row de la colonne, cmme la fonction lambda avt)
def getElement(myList, position): 
    return myList[position]
netteBad.price_adult_max.astype(str).str.split('.').apply(getElement, position=0)

# PLOT TUTO


