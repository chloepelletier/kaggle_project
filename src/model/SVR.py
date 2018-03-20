import pandas as pd
from sklearn import svm
    
training_set = pd.read_csv('data/processed/training_set_bis.csv')
training_set.drop(['Unnamed: 0','date', 'year'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)


validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.drop(['Unnamed: 0','date', 'year'], axis=1, inplace=True)
validation_set.dropna(how='any', inplace=True)

# Remplacer les str par int pour les variables ordinale
training_set.snow_height = pd.factorize(training_set['snow_height'])[0]
training_set.precipitation = pd.factorize(training_set['precipitation'])[0]
training_set.Price = pd.factorize(training_set['Price'])[0]
training_set.sunshine_radiation = pd.factorize(training_set['sunshine_radiation'])[0]
training_set.wind_speed_max = pd.factorize(training_set['wind_speed_max'])[0]

validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]
validation_set.precipitation = pd.factorize(validation_set['precipitation'])[0]
validation_set.Price = pd.factorize(validation_set['Price'])[0]
validation_set.sunshine_radiation = pd.factorize(validation_set['sunshine_radiation'])[0]
validation_set.wind_speed_max = pd.factorize(validation_set['wind_speed_max'])[0]

y = training_set.visitors_pool_total.values.astype(int)

feature = ['sportbad_closed', 'freizeitbad_closed','sauna_closed', 'kursbecken_closed', 'event', 'sloop_dummy','school_holiday', 'bank_holiday', 'Price', 'precipitation','sunshine_radiation', 'temperature', 'wind_speed_max', 'snow_height','day', 'day_bis']
feature = ['sloop_dummy','month', 'day_bis', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed',  'school_holiday',  'bank_holiday', 'temperature',  'snow_height']


# SVR
clf = svm.LinearSVR(loss='squared_epsilon_insensitive', max_iter=160, dual=False)

# Entrainement
clf.fit(training_set[feature], y)

# Prediction
result = clf.predict(validation_set[feature])


from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(validation_set.visitors_pool_total.values.astype(int), result))


