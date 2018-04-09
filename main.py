import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error


# Charger les fichiers csv
import src.data.getDataFrames
import src.data.getDataFramesSubmission

# Importe les dataframes
training_set = pd.read_csv('data/processed/training_set.csv')
training_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)

validation_set = pd.read_csv('data/processed/validation_set.csv')
validation_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
validation_set.dropna(how='any', inplace=True)

test_set = pd.read_csv('data/processed/test_set.csv')
test_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
test_set.dropna(how='any', inplace=True)

submission_set = pd.read_csv('data/processed/submission_set.csv')
submission_set.drop(['Unnamed: 0','date', 'year', 'precipitation'], axis=1, inplace=True)
submission_set.dropna(how='any', inplace=True)

# Récupération des tableaux énumérant le nombre de visiteurs total
valide_train      = training_set.visitors_pool_total.values.astype(int)
valide_validation = validation_set.visitors_pool_total.values.astype(int)
valide_test       = test_set.visitors_pool_total.values.astype(int)

training_set.drop(['visitors_pool_total'], axis=1, inplace=True)

# MODELE Random Forest Regression 
feature = ['month', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed', 'sloop_dummy', 'school_holiday',  'bank_holiday', 'temperature', 'day_bis']

X_train      = training_set[feature]
X_validation = validation_set[feature]
X_test       = test_set[feature]
X_submission = submission_set[feature]

regr = RandomForestRegressor(random_state=0, n_jobs=-1, max_depth=9, min_samples_split= 20, min_samples_leaf= 3)
regr.fit(X_train, valide_train)

result_vald = regr.predict(X_validation)
result_test = regr.predict(X_test)
result_subm = regr.predict(X_submission)

# MODELE Multi Layer Perceptron Classifier 
feature = ['month', 'temperature','day', 'day_bis', 'sportbad_closed', 'freizeitbad_closed', 'kursbecken_closed', 'event', 'sloop_dummy', 'school_holiday', 'bank_holiday']

X_train = training_set[feature]
X_validation = validation_set[feature]
X_test = test_set[feature]
X_submission = submission_set[feature]

mlp = MLPRegressor(hidden_layer_sizes=(200, 200, 200, 200, 200, 200), max_iter=100, alpha=.5, batch_size=10, learning_rate_init=0.0005, random_state=1)
mlp.fit(X_train, valide_train)

result_vald_bis = mlp.predict(X_validation)
result_test_bis = mlp.predict(X_test)
result_subm_bis = mlp.predict(X_submission)

# Récupération de la prédiction la plus faible
res_min = []

for i in range(0, len(result_vald)):
    if result_vald[i] < result_vald_bis[i]:
        res_min.append(result_vald_bis[i])
    else:
        res_min.append(result_vald[i])
    
# Score du jeu de validation
np.sqrt(mean_squared_error(valide_validation, res_min))

# TEST SET
res_test_min = []

for i in range(0, len(result_test)):
    if result_test[i] < result_test_bis[i]:
        res_test_min.append(result_test_bis[i])
    else:
        res_test_min.append(result_test[i])
        
np.sqrt(mean_squared_error(valide_test, res_test_min))

# SUBMISSION TEST
res_subm_min = []

for i in range(0, len(result_subm)):
    if result_subm[i] < result_subm_bis[i]:
        res_subm_min.append(result_subm_bis[i])
    else:
        res_subm_min.append(result_subm[i])
        
submission_example = pd.read_csv('data/raw/sample_submission_nettebad.csv')
submission_example.visitors_pool_total = res_subm_min
submission_example.to_csv("data/processed/submission.csv")
