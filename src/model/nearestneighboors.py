

import pandas as pd
from sklearn import neighbors
import numpy as np


training_set = pd.read_csv('data/processed/training_set_bis.csv')
def getNbClasse(nb):
    return int((nb+50)/100)*100
training_set.snow_height = pd.factorize(training_set['snow_height'])[0]
training_set.precipitation = pd.factorize(training_set['precipitation'])[0]
training_set.Price = pd.factorize(training_set['Price'])[0]
training_set.sunshine_radiation = pd.factorize(training_set['sunshine_radiation'])[0]
training_set.wind_speed_max = pd.factorize(training_set['wind_speed_max'])[0]
training_set.drop(['precipitation'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)
training_set['visitors_pool_total'] = training_set.apply(lambda row: getNbClasse(row['visitors_pool_total']), axis=1)



X = training_set.as_matrix(columns= ['day', 'day_bis', 'school_holiday', 'bank_holiday'
                                     ,'sportbad_closed', 'freizeitbad_closed',
       'kursbecken_closed','temperature', 'snow_height','month'])
y = np.array(training_set['visitors_pool_total'])

clf = neighbors.KNeighborsClassifier(10, weights = 'distance',leaf_size =1)
trained_model = clf.fit(X, y)

trained_model.score(X, y)


validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.dropna(how='any', inplace=True)
validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]
validation_set.precipitation = pd.factorize(validation_set['precipitation'])[0]
validation_set.Price = pd.factorize(validation_set['Price'])[0]
validation_set.sunshine_radiation = pd.factorize(validation_set['sunshine_radiation'])[0]
validation_set.wind_speed_max = pd.factorize(validation_set['wind_speed_max'])[0]
validation_set.drop(['Unnamed: 0','date', 'year','visitors_pool_total','precipitation',
                     'Price','wind_speed_max','sauna_closed','event','sloop_dummy',
                     'sunshine_radiation'], axis=1, inplace=True)
    
validation_set = validation_set[['day', 'day_bis', 'school_holiday', 'bank_holiday'
                                ,'sportbad_closed', 'freizeitbad_closed',
                                'kursbecken_closed','temperature', 'snow_height','month']]

test = validation_set.values.astype(int)
result=trained_model.predict(test)


validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.dropna(how='any', inplace=True)
from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(validation_set.visitors_pool_total.values.astype(int), result))


    
   
    