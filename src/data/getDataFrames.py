import pandas as pd

netteBad           = pd.read_csv('data/raw/nettebad_train_set.csv', sep=';')
weather_dwd        = pd.read_csv('data/raw/weather_dwd_train_set.csv', sep=';')
weather_osnabrueck = pd.read_csv('data/raw/weather_uni_osnabrueck_train_set.csv', sep=';')

# Formatage des dates
netteBad.date           = pd.to_datetime(netteBad.date, format='%m/%d/%Y')
weather_dwd.date        = pd.to_datetime(weather_dwd.date, format='%m/%d/%Y')
weather_osnabrueck.date = pd.to_datetime(weather_osnabrueck.date, format='%d/%m/%Y')

netteBad           = netteBad.sort_values(by=['date'])
weather_dwd        = weather_dwd.sort_values(by=['date'])
weather_osnabrueck = weather_osnabrueck.sort_values(by=['date'])


# Création des intervalles : tarif
def getPriceClasse(price_adult_90min, price_adult_max, price_reduced_90min, price_reduced_max):
    if price_adult_90min   == 3.2 and price_adult_max  == 6.7 and price_reduced_90min == 1.7 and price_reduced_max  == 3.7:
        return 'P1'
    elif price_adult_90min == 4.3 and price_adult_max  == 7.3 and price_reduced_90min == 2.3 and price_reduced_max  == 4.3:
        return 'P2'
    elif price_adult_90min == 4.6 and price_adult_max  == 7.6 and price_reduced_90min == 2.6 and price_reduced_max  == 4.6:
        return 'P3'
    elif price_adult_90min == 4.6 and price_adult_max  == 10 and price_reduced_90min  == 2.8 and price_reduced_max  == 8.3:
        return 'P4'
    elif price_adult_90min == 4.9 and price_adult_max  == 10 and price_reduced_90min  == 3.1 and price_reduced_max  == 8.3:
        return 'P5'
    elif price_adult_90min == 5.2  and price_adult_max == 10 and price_reduced_90min  == 3.3  and price_reduced_max == 8.3:
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

#création des intervalles pour la hauteur de précipitation
def getPrecipitationClasse(precipitation):
    if precipitation   >= 0  and precipitation < 2 :
        return 'P0'
    elif precipitation >= 2  and precipitation < 8 :
        return 'P1'
    else :
        return 'P2'   
    
weather_dwd['precipitation_DWD'] = weather_dwd.apply(lambda row: getPrecipitationClasse(row['precipitation_DWD']), axis=1)
    
# Transformation des nb d'heure en radiation 
def getRadiation(hour):
    return hour*21.45+51.24

weather_dwd['radiation'] = weather_dwd.apply(lambda row: getRadiation(row['sunshine_hours_DWD']), axis=1)
weather_dwd.drop('sunshine_hours_DWD', axis=1, inplace=True)

# Création d'intervalles : radiation solaire 
def getSunshineClasse(global_solar_radiation_UniOS):
    if global_solar_radiation_UniOS >= 0   and global_solar_radiation_UniOS < 100:
        return 'RS0'
    if global_solar_radiation_UniOS >= 100 and global_solar_radiation_UniOS < 200:
        return 'RS1'
    if global_solar_radiation_UniOS >= 200 and global_solar_radiation_UniOS < 300:
        return 'RS2'
    else :
        return 'RS3'

weather_osnabrueck['sunshine_radiation'] = weather_osnabrueck.apply(lambda row: getSunshineClasse(row['global_solar_radiation_UniOS']), axis=1)
weather_dwd['sunshine_radiation']        = weather_dwd.apply(lambda row: getSunshineClasse(row['radiation']), axis=1)

# Création d'intervalles : vitesse du vent maximale
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
weather_dwd['wind_speed_max_DWD']          = weather_dwd.apply(lambda row: getWindClasse(row['wind_speed_max_DWD']), axis=1)

# Suppression des colonnes inutiles pour le fichier nettebad 
netteBad.drop(['sloop_dummy', 'price_adult_90min', 'price_adult_max', 'price_reduced_90min', 'price_reduced_max'], axis=1, inplace=True)

# Suppression des colonnes inutiles dans weather_dwd + renommage
weather_dwd.drop(['air_humidity_DWD', 'air_temperature_daily_max_DWD', 'air_temperature_daily_min_DWD', 'radiation'], axis=1, inplace=True)
weather_dwd.columns = ['date', 'temperature', 'precipitation', 'snow_height', 'wind_speed_max', 'sunshine_radiation']

# Suppresion des colonnes inutiles dans weather_osnabrueck + renommage
weather_osnabrueck.drop(['air_humidity_UniOS', 'air_pressure_UniOS', 'global_solar_radiation_UniOS', 'wind_direction_category_UniOS', 'wind_speed_avg_UniOS'], axis=1, inplace=True)
weather_osnabrueck.columns = ['date', 'temperature', 'wind_speed_max', 'sunshine_radiation']

# Fusion de dataframes
weather_dwd_2 = weather_dwd[['date', 'precipitation', 'snow_height']]
weather_dwd.drop(['precipitation', 'snow_height'], axis=1, inplace=True)

weather_dwd['year'] = weather_dwd.date.apply(lambda x: x.year)
weather_dwd         = weather_dwd[weather_dwd.year < 2010]
weather_dwd.drop('year', axis=1, inplace=True)

weather = pd.concat([weather_dwd, weather_osnabrueck])

netteBad = pd.merge(netteBad, weather, on='date', how='outer')
netteBad = pd.merge(netteBad, weather_dwd_2, on='date', how='outer')
netteBad = netteBad.sort_values(by=['date'])

netteBad['year']  = netteBad.date.apply(lambda x: x.year)
netteBad['month'] = netteBad.date.apply(lambda x: x.month)
netteBad          = netteBad[(netteBad.year != 2005) | (netteBad.month.isin(['4', '5', '6', '7', '8', '9', '10', '11', '12']))]

# Récupération des data frames de training/validation/test
training_set    = netteBad[(netteBad.year != 2008) & (netteBad.year != 2011)]
validation_set  = netteBad[netteBad.year == 2008]
test_set        = netteBad[netteBad.year == 2011]

training_set.drop(['year', 'month'], axis=1, inplace=True)
validation_set.drop(['year', 'month'], axis=1, inplace=True)
test_set.drop(['year', 'month'], axis=1, inplace=True)

training_set.to_csv("data/processed/training_set.csv")
validation_set.to_csv("data/processed/validation_set.csv")
test_set.to_csv("data/processed/test_set.csv")


