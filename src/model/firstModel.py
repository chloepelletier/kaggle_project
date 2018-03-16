# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Set random seed
np.random.seed(0)

# Random forest

training_set = pd.read_csv('data/processed/training_set.csv')
training_set.drop(['Unnamed: 0','date', 'year', 'month'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)

validation_set = pd.read_csv('data/processed/validation_set.csv')
validation_set.drop(['Unnamed: 0','date', 'year','month'], axis=1, inplace=True)
validation_set.dropna(how='any', inplace=True)

# Create a list of the feature column's names
features = training_set.columns[:10]

# View features
features


y = training_set.visitors_pool_total.values.astype(int)

training_set.snow_height = pd.factorize(training_set['snow_height'])[0]
training_set.sunshine_radiation = pd.factorize(training_set['sunshine_radiation'])[0]
validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]
validation_set.sunshine_radiation = pd.factorize(validation_set['sunshine_radiation'])[0]


# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)
clf.fit(training_set[features], y)


result = clf.predict(validation_set[features])
from sklearn.metrics import mean_squared_error
rms = np.sqrt(mean_squared_error(validation_set.visitors_pool_total.values.astype(int), result))
print(rms)




