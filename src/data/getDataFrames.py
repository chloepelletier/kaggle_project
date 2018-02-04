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

# Gestion des données manquantes et fusion des dataframes
weather_dwd['year'] = weather_dwd.date.apply(lambda x: x.year)
weather_dwd = weather_dwd[weather_dwd.year < 2010]
weather_dwd.drop(['air_temperature_daily_max_DWD', 'air_temperature_daily_min_DWD', 'precipitation_DWD', 'snow_height_DWD', 'sunshine_hours_DWD', 'year'], axis=1, inplace=True)
weather_dwd.columns = ['date', 'air_humidity', 'temperature', 'vitesse maximale du vent']

weather_osnabrueck['year'] = weather_osnabrueck.date.apply(lambda x: x.year)
weather_osnabrueck = weather_osnabrueck[weather_osnabrueck.year > 2009]
weather_osnabrueck.drop(['air_pressure_UniOS', 'global_solar_radiation_UniOS', 'wind_speed_avg_UniOS', 'wind_direction_category_UniOS', 'year'], axis=1, inplace=True)
weather_osnabrueck.columns = ['date', 'air_humidity', 'temperature', 'vitesse maximale du vent']

weather = pd.concat([weather_dwd, weather_osnabrueck])

result = pd.merge(netteBad, weather, on='date', how='outer')
result = result.sort_values(by=['date'])
