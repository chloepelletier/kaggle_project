from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

training_set = pd.read_csv('data/processed/training_set_bis.csv')
training_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)

validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
validation_set.dropna(how='any', inplace=True)
valide = validation_set.visitors_pool_total

# Remplacer les str par int pour les variables ordinale
training_set.snow_height = pd.factorize(training_set['snow_height'])[0]
training_set.Price = pd.factorize(training_set['Price'])[0]
training_set.sunshine_radiation = pd.factorize(training_set['sunshine_radiation'])[0]
training_set.wind_speed_max = pd.factorize(training_set['wind_speed_max'])[0]

validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]
validation_set.Price = pd.factorize(validation_set['Price'])[0]
validation_set.sunshine_radiation = pd.factorize(validation_set['sunshine_radiation'])[0]
validation_set.wind_speed_max = pd.factorize(validation_set['wind_speed_max'])[0]

# Create a list of the feature column's names
y = training_set.visitors_pool_total.values.astype(int)
training_set.drop(['visitors_pool_total'], axis=1, inplace=True)

feature = ['sportbad_closed', 'freizeitbad_closed','sauna_closed', 'kursbecken_closed', 'event', 'sloop_dummy','school_holiday', 'bank_holiday', 'Price','sunshine_radiation', 'temperature', 'wind_speed_max', 'snow_height','day', 'day_bis']
feature = ['month', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed', 'sloop_dummy', 'school_holiday',  'bank_holiday', 'temperature',  'snow_height', 'day_bis']

# preprocessing
scaler = StandardScaler()

scaler.fit(training_set[feature])

X_train = scaler.transform(training_set[feature])
X_test = scaler.transform(validation_set[feature])

# without preprocessing
X_train = training_set[feature]
X_test = validation_set[feature]

# Multi Layer Perceptron Classifier
# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(13,13,13),max_iter=500)

# Entrainement
mlp.fit(X_train, y)

# Prediction
result = mlp.predict(X_test)

# Tests
np.sqrt(mean_squared_error(valide.values.astype(int), result))



