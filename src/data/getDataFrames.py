netteBad = pd.read_csv('data/raw/nettebad_train_set.csv', sep=';')
weather_dwd = pd.read_csv('data/raw/weather_dwd_train_set.csv', sep=';')
weather_osnabrueck = pd.read_csv('data/raw/weather_uni_osnabrueck_train_set.csv', sep=';')

# Formatage des dates
from datetime import datetime
netteBad.date = pd.to_datetime(netteBad.date, format='%m/%d/%Y')
weather_dwd.date = pd.to_datetime(weather_dwd.date, format='%m/%d/%Y')
weather_osnabrueck.date = pd.to_datetime(weather_osnabrueck.date, format='%d/%m/%Y')

netteBad = netteBad.sort_values(by=['date'])
weather_dwd = weather_dwd.sort_values(by=['date'])
weather_osnabrueck = weather_osnabrueck.sort_values(by=['date'])

# Création d'intervalles
def getPriceClasse(price_adult_90min, price_adult_max, price_reduced_90min, price_reduced_max):
    if price_adult_90min == 3.2 and price_adult_max == 6.7 and price_reduced_90min == 1.7 and price_reduced_max == 3.7:
        return 'P1'
    elif price_adult_90min == 4.3 and price_adult_max == 7.3 and price_reduced_90min == 2.3 and price_reduced_max == 4.3:
        return 'P2'
    elif price_adult_90min == 4.6 and price_adult_max == 7.6 and price_reduced_90min == 2.6 and price_reduced_max == 4.6:
        return 'P3'
    elif price_adult_90min == 4.6 and price_adult_max == 10 and price_reduced_90min == 2.8 and price_reduced_max == 8.3:
        return 'P4'
    elif price_adult_90min == 4.9 and price_adult_max == 10 and price_reduced_90min == 3.1 and price_reduced_max == 8.3:
        return 'P5'
    elif price_adult_90min == 5.2  and price_adult_max == 10 and price_reduced_90min == 3.3  and price_reduced_max == 8.3:
        return 'P6'
    else :
        return 'P0'
    
netteBad['Price'] = netteBad.apply(lambda row: getPriceClasse(row['price_adult_90min'], row['price_adult_max'], row['price_reduced_90min'], row['price_reduced_max']), axis=1)

def getSunshineClasseDWD(sunshine_hours_DWD):
    if sunshine_hours_DWD >= 0 and sunshine_hours_DWD < 0:
        return '0'
    if sunshine_hours_DWD >= 0 and sunshine_hours_DWD < 4:
        return '1'
    if sunshine_hours_DWD >= 4 and sunshine_hours_DWD < 6:
        return '2'
    if sunshine_hours_DWD >= 6 and sunshine_hours_DWD < 8:
        return '3'
    else :
        return '4'

weather_dwd['sunshine'] = weather_dwd.apply(lambda row: getSunshineClasseDWD(row['sunshine_hours_DWD']), axis=1)

def getSunshineClasseOSNABRUECK(global_solar_radiation_UniOS):
    if global_solar_radiation_UniOS >= 0 and global_solar_radiation_UniOS < 25.43:
        return '0'
    if global_solar_radiation_UniOS >= 25.43 and global_solar_radiation_UniOS < 29.37:
        return '1'
    if global_solar_radiation_UniOS >= 29.37 and global_solar_radiation_UniOS < 36.54:
        return '2'
    if global_solar_radiation_UniOS >= 36.54 and global_solar_radiation_UniOS < 900:
        return '3'
    else :
        return '4'

weather_osnabrueck['sunshine_radiation'] = weather_osnabrueck.apply(lambda row: getSunshineClasseOSNABRUECK(row['global_solar_radiation_UniOS']), axis=1)


def getWindClasse(wind):
    wind = wind * 3.6
    if wind < 12:
        return '1'
    if wind >= 12 and wind < 29:
        return '2'
    if wind >= 29 and wind < 50:
        return '3'
    if wind >= 50 and wind < 89:
        return '4'
    else :
        return '5'

weather_osnabrueck['wind_speed_max_UniOS'] = weather_osnabrueck['wind_speed_max_UniOS'].apply(lambda x: x*0.2286828398051166+1.320735954229235)
weather_osnabrueck['wind_speed_max_UniOS'] = weather_osnabrueck.apply(lambda row: getWindClasse(row['wind_speed_max_UniOS']), axis=1)
weather_dwd['wind_speed_max_DWD'] = weather_dwd.apply(lambda row: getWindClasse(row['wind_speed_max_DWD']), axis=1)



# Comparaison de l'ensoleillement weather
weather_dwd['year'] = weather_dwd.date.apply(lambda x: x.year)
weather_dwd['month'] = weather_dwd.date.apply(lambda x: x.month)
weather_dwd['day'] = weather_dwd.date.apply(lambda x: x.day)
weather_dwd = weather_dwd[((weather_dwd.year == 2009) & (weather_dwd.month.isin([7, 8, 9, 10, 11, 12]))) | ((weather_dwd.year == 2010) & (weather_dwd.month.isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) ]
weather_dwd = weather_dwd[['date', 'wind_speed_max_DWD']]


weather_osnabrueck['year'] = weather_osnabrueck.date.apply(lambda x: x.year)
weather_osnabrueck['month'] = weather_osnabrueck.date.apply(lambda x: x.month)
weather_osnabrueck['day'] = weather_osnabrueck.date.apply(lambda x: x.day)
weather_osnabrueck = weather_osnabrueck[((weather_osnabrueck.year == 2009) & (weather_osnabrueck.month.isin([7, 8, 9, 10, 11, 12]))) | ((weather_osnabrueck.year == 2010) & (weather_osnabrueck.month.isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) ]
weather_osnabrueck = weather_osnabrueck[['date', 'wind_speed_max_UniOS']]

weather = pd.merge(weather_osnabrueck, weather_dwd, on='date', how='outer')
weather = weather.sort_values(by=['date'])
weather.drop(['date'], axis=1, inplace=True)

from scipy import stats
import numpy as np
y = weather['wind_speed_max_DWD']
x = weather['wind_speed_max_UniOS']
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

weather.corr()
weather['newMax'] = weather['wind_speed_max_UniOS'].apply(lambda x: x*slope+intercept)



sameWindClasse = weather[weather.wind_speed_max_DWD == weather.wind_speed_avg_UniOS]
sameWindClasse.shape[0] / weather.shape[0] * 100


sameWindClasse1 = weather[weather.wind_speed_max_DWD.astype(float) - weather.wind_speed_avg_UniOS.astype(float) == 0]
sameWindClasse3 = weather[weather.wind_speed_max_DWD.astype(float) - weather.wind_speed_avg_UniOS.astype(float) == 1]
sameWindClasse2 = weather[weather.wind_speed_max_DWD.astype(float) - weather.wind_speed_avg_UniOS.astype(float) == -1]
(sameWindClasse1.shape[0] + sameWindClasse2.shape[0] + sameWindClasse3.shape[0]) / weather.shape[0] * 100



# Suppression des colonnes inutiles pour le fichier nettebad 
netteBad.drop('sloop_dummy', axis=1, inplace=True)
netteBad.drop('price_adult_90min', axis=1, inplace=True)
netteBad.drop('price_adult_max', axis=1, inplace=True)
netteBad.drop('price_reduced_90min', axis=1, inplace=True)
netteBad.drop('price_reduced_max', axis=1, inplace=True)

# Suppression des colonnes inutiles dans weather_dwd
weather_dwd.drop('air_humidity_DWD', axis=1, inplace=True)
weather_dwd.drop('air_temperature_daily_max_DWD', axis=1, inplace=True)
weather_dwd.drop('air_temperature_daily_min_DWD', axis=1, inplace=True)

# Suppresion des colonnes inutiles dans weather_osnabrueck
weather_osnabrueck.drop('air_humidity_UniOS', axis=1, inplace=True)
weather_osnabrueck.drop('air_pressure_UniOS', axis=1, inplace=True)
weather_osnabrueck.drop('wind_direction_category_UniOS', axis=1, inplace=True)

# Regarde si les 2 df de weather se ressemblent
weather_dwd['year'] = weather_dwd.date.apply(lambda x: x.year)
weather_dwd['month'] = weather_dwd.date.apply(lambda x: x.month)
weather_dwd['day'] = weather_dwd.date.apply(lambda x: x.day)
weather_dwd = weather_dwd[((weather_dwd.year == 2009) & (weather_dwd.month.isin([7, 8, 9, 10, 11, 12]))) | ((weather_dwd.year == 2010) & (weather_dwd.month.isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) ]
weather_dwd.drop(['air_temperature_daily_max_DWD', 'air_temperature_daily_min_DWD', 'precipitation_DWD', 'snow_height_DWD', 'sunshine_hours_DWD', 'year', 'month', 'day'], axis=1, inplace=True)
weather_dwd.columns = ['date', 'air_humidity_1', 'temperature_1', 'wind_speed_max_1']

weather_osnabrueck['year'] = weather_osnabrueck.date.apply(lambda x: x.year)
weather_osnabrueck['month'] = weather_osnabrueck.date.apply(lambda x: x.month)
weather_osnabrueck['day'] = weather_osnabrueck.date.apply(lambda x: x.day)
weather_osnabrueck = weather_osnabrueck[((weather_osnabrueck.year == 2009) & (weather_osnabrueck.month.isin([7, 8, 9, 10, 11, 12]))) | ((weather_osnabrueck.year == 2010) & (weather_osnabrueck.month.isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) ]
weather_osnabrueck.drop(['air_pressure_UniOS', 'global_solar_radiation_UniOS', 'wind_speed_avg_UniOS', 'wind_direction_category_UniOS', 'year', 'month', 'day'], axis=1, inplace=True)
weather_osnabrueck.columns = ['date', 'air_humidity_2', 'temperature_2', 'wind_speed_max_2']

result = pd.merge(weather_osnabrueck, weather_dwd, on='date', how='outer')
result['air_humidity'] = np.abs(result.air_humidity_1.astype('float') - result.air_humidity_2.astype('float'))
result['wind_speed_max'] = np.abs(result.wind_speed_max_1.astype('float') - result.wind_speed_max_2.astype('float'))
result['temperature'] = np.abs(result.temperature_1.astype('float') - result.temperature_2.astype('float'))

result.temperature.mean()
result.air_humidity.mean()
result.wind_speed_max.mean()

# Gestion des données manquantes et fusion des dataframes
weather_dwd['year'] = weather_dwd.date.apply(lambda x: x.year)
weather_dwd = weather_dwd[weather_dwd.year < 2010]
weather_dwd.drop(['air_temperature_daily_max_DWD', 'air_temperature_daily_min_DWD', 'precipitation_DWD', 'snow_height_DWD', 'sunshine_hours_DWD', 'year'], axis=1, inplace=True)
weather_dwd.columns = ['date', 'air_humidity', 'temperature', 'wind_speed_max']

weather_osnabrueck['year'] = weather_osnabrueck.date.apply(lambda x: x.year)
weather_osnabrueck = weather_osnabrueck[weather_osnabrueck.year > 2009]
weather_osnabrueck.drop(['air_pressure_UniOS', 'global_solar_radiation_UniOS', 'wind_speed_avg_UniOS', 'wind_direction_category_UniOS', 'year'], axis=1, inplace=True)
weather_osnabrueck.columns = ['date', 'air_humidity', 'temperature', 'wind_speed_max']

weather = pd.concat([weather_dwd, weather_osnabrueck])

result = pd.merge(netteBad, weather, on='date', how='outer')
result = result.sort_values(by=['date'])
