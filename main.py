import pandas as pd
import numpy as np
import sklearn as skl
from matplotlib import pyplot as ppl

import src.data.getDataFrames


# PANDA TUTO

# Lire un fichier csv en data frame: (on peut changer les noms de colonnes direct)
pd.read_csv('data/raw/weather_dwd_train_set.csv', sep=';')
# Connaitre les 5 premieres:
netteBad.head()
# Connaitre le nombre de colonnes et lignes:
netteBad.shape
# Stat basique, moyenne, std, min, etc sur chaque colonnes:
netteBad.describe()
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
# faire un filter sur une colonne:
netteBadWith1482Or23Visitors = netteBad[netteBad['visitors_pool_total'].isin(['1482', '23'])]
netteBadWithMoreThan482Visitors = netteBad[netteBad.visitors_pool_total >= 482]
# Utiliser plusieurs filtres:
netteBadWithMoreThan482VisitorsAndEvent = netteBad[(netteBad.visitors_pool_total >= 1182) & (netteBad.event == 1)]
netteBadWithMoreThan482VisitorsAndEvent = netteBad[(netteBad.visitors_pool_total >= 482) | (netteBad.event == 1)]
# fire un filter et ne selectionner que certaines colonnes:
visitorWithMoreThan482Visitors = netteBad[netteBad.visitors_pool_total >= 482].visitors_pool_total
visitorWithMoreThan482Visitors = netteBad.loc[netteBad.visitors_pool_total >= 482, 'visitors_pool_total']
visitorWithMoreThan482Visitors = netteBad.loc[netteBad.visitors_pool_total >= 482, ['visitors_pool_total', 'date']]
