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

# Suppression de la colonne sloop dummy inutile
netteBad.drop('sloop_dummy', axis=1, inplace=True)

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
