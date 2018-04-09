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

feature = ['month', 'temperature','day', 'day_bis', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed', 'event', 'sloop_dummy', 'school_holiday', 'bank_holiday']

X_train = training_set[feature]
X_test = validation_set[feature]
valide = validation_set.visitors_pool_total

# Multi Layer Perceptron Classifier
# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(200, 200, 200, 200, 200, 200), max_iter=100, alpha=.5, batch_size=10, learning_rate_init=0.0005, random_state=1)

# Entrainement
mlp.fit(X_train, y)

# Prediction
result = mlp.predict(X_test)

# Tests
np.sqrt(mean_squared_error(valide.values.astype(int), result))

