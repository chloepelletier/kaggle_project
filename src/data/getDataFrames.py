netteBad = pd.read_csv('../../data/raw/nettebad_train_set.csv', sep=';')
weather_dwd = pd.read_csv('../../data/raw/weather_dwd_train_set.csv', sep=';')
weather_osnabrueck = pd.read_csv('../../data/raw/weather_uni_osnabrueck_train_set.csv', sep=';')


# Formatage des dates
from datetime import datetime
netteBad.date = pd.to_datetime(netteBad.date, format='%m/%d/%Y')
weather_dwd.date = pd.to_datetime(weather_dwd.date, format='%m/%d/%Y')
weather_osnabrueck.date = pd.to_datetime(weather_osnabrueck.date, format='%d/%m/%Y')

netteBad = netteBad.sort_values(by=['date'])
weather_dwd = weather_dwd.sort_values(by=['date'])
weather_osnabrueck = weather_osnabrueck.sort_values(by=['date'])

print(type(netteBad.sportbad_closed[0]))

# Gestion des données manquantes

