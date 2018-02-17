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

#création des intervalles pour la hauteur de neige 
def getSnowClasse(snow_height):
    if snow_height == 0 :
        return 'S0'
    else :
        return 'S1'
    
weather_dwd['snow_height_DWD'] = weather_dwd.apply(lambda row: getSnowClasse(row['snow_height_DWD']), axis=1)

#création des intervalles pour la hauteur de neige 
def getPrecipitationClasse(precipitation):
    if precipitation>=0 and precipitation<2 :
        return 'P0'
    elif precipitation>=2 and precipitation<12 :
        return 'P1'
    elif precipitation>=12 and precipitation<48 :
        return 'P2'
    elif precipitation>=48 and precipitation<96 :
        return 'P3'
    else :
        return 'P4'   
    
weather_dwd['precipitation_DWD'] = weather_dwd.apply(lambda row: getPrecipitationClasse(row['precipitation_DWD']), axis=1)

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
