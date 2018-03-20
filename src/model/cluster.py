from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

def getNbClasse(nb):
    return int((nb+50)/100)*100

training_set = pd.read_csv('data/processed/training_set_bis.csv')

#training_set['visitors_pool_total'] = training_set.apply(lambda row: getNbClasse(row['visitors_pool_total']), axis=1)
nbClasse = training_set['visitors_pool_total'].unique().size
training_set.drop(['Unnamed: 0','date', 'year','sauna_closed','event','sloop_dummy','Price','precipitation','sunshine_radiation','wind_speed_max'], axis=1, inplace=True)
training_set.dropna(how='any', inplace=True)
training_set_bis = pd.DataFrame(training_set.visitors_pool_total)
training_set.drop(['visitors_pool_total'], axis=1, inplace=True)

# Remplacer les str par int pour les variables ordinale
training_set.snow_height = pd.factorize(training_set['snow_height'])[0]


# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(training_set)

# Create k-mean object
clt = KMeans(n_clusters=100, random_state=0, n_jobs=1)

# Train model
model = clt.fit(X_std)
training_set_bis['cluster'] = model.labels_
mes_clusters = training_set_bis.groupby('cluster').mean()

training_set_bis.plot(x='cluster',y='visitors_pool_total',kind='scatter')

validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.dropna(how='any', inplace=True)
validation_set.drop(['Unnamed: 0','visitors_pool_total','date','year','sauna_closed','event','sloop_dummy','Price','precipitation','sunshine_radiation','wind_speed_max'], axis=1, inplace=True)
validation_set.snow_height = pd.factorize(validation_set['snow_height'])[0]

test = validation_set.values.astype(int)
result['group']=pd.DataFrame(model.predict(test))
def getgood(nb):
    return mes_clusters.visitors_pool_total[nb]
result['visitors'] = result.apply(lambda row: getgood(row['group']), axis=1)

validation_set = pd.read_csv('data/processed/validation_set_bis.csv')
validation_set.dropna(how='any', inplace=True)
from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(validation_set.visitors_pool_total.values.astype(int), result.visitors))




    