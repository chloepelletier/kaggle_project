from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectFromModel
import pandas as pd
import numpy as np

def getNbClasses(nb):
    return int((nb+10)/100)*100

training_set = pd.read_csv('data/processed/training_set_bis.csv')
training_set.drop(['Unnamed: 0','date', 'year'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)
training_set['visitors_pool_total'] = training_set.apply(lambda row: getNbClasses(row['visitors_pool_total']), axis=1)

validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.dropna(how='any', inplace=True)
valide = validation_set.visitors_pool_total
validation_set.drop(['Unnamed: 0','date', 'year', 'visitors_pool_total'], axis=1, inplace=True)

# Remplacer les str par int pour les variables ordinale
training_set.snow_height = pd.factorize(training_set['snow_height'])[0]
#training_set.precipitation = pd.factorize(training_set['precipitation'])[0]
training_set.Price = pd.factorize(training_set['Price'])[0]
training_set.sunshine_radiation = pd.factorize(training_set['sunshine_radiation'])[0]
training_set.wind_speed_max = pd.factorize(training_set['wind_speed_max'])[0]

validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]
#validation_set.precipitation = pd.factorize(validation_set['precipitation'])[0]
validation_set.Price = pd.factorize(validation_set['Price'])[0]
validation_set.sunshine_radiation = pd.factorize(validation_set['sunshine_radiation'])[0]
validation_set.wind_speed_max = pd.factorize(validation_set['wind_speed_max'])[0]

# Create a list of the feature column's names
y = training_set.visitors_pool_total.values.astype(int)
training_set.drop(['visitors_pool_total'], axis=1, inplace=True)

feature = ['sportbad_closed', 'freizeitbad_closed','sauna_closed', 'kursbecken_closed', 'event', 'sloop_dummy','school_holiday', 'bank_holiday', 'Price', 'sunshine_radiation', 'temperature', 'wind_speed_max', 'snow_height','day', 'day_bis']
feature = ['month', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed', 'sloop_dummy', 'school_holiday',  'bank_holiday', 'temperature',  'snow_height', 'day_bis']

# Random Forest Classifier
clf = RandomForestClassifier(n_jobs=-1, random_state=0, max_depth=9, min_samples_split=20)

# Entrainement
clf.fit(training_set[feature], y)

# Prediction
result = clf.predict(validation_set[feature])


# Si l'on veut mettre un seuil pour choisir automatiquement les features à utiliser
#selector = SelectFromModel(clf, threshold=.01)
#training_set_important = selector.fit_transform(training_set[feature], y)
#clf.fit(training_set_important, y)

#feature_idx = selector.get_support()
#featureBis = training_set[feature].columns[feature_idx]

#result = clf.predict(validation_set[featureBis])

# Tests
np.sqrt(mean_squared_error(valide.values.astype(int), result))






