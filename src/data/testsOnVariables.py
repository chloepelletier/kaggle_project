import pandas as pd

training_set = pd.read_csv('data/processed/training_set.csv')
training_set.drop(['Unnamed: 0'], axis=1, inplace=True)

# =====================================================================================
# test pour savoir si les catégories des attribus sont différentes - test kruskalwallis
# =====================================================================================
from scipy import stats

# JOUR DE LA SEMAINE
training_set_mon = training_set[training_set.day == 0].visitors_pool_total.dropna(how='any')
training_set_tue = training_set[training_set.day == 1].visitors_pool_total.dropna(how='any')
training_set_wen = training_set[training_set.day == 2].visitors_pool_total.dropna(how='any')
training_set_thu = training_set[training_set.day == 3].visitors_pool_total.dropna(how='any')
training_set_fri = training_set[training_set.day == 4].visitors_pool_total.dropna(how='any')
training_set_sat = training_set[training_set.day == 5].visitors_pool_total.dropna(how='any')
training_set_sun = training_set[training_set.day == 6].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_mon.values, training_set_tue.values)[1]
stats.kruskal(training_set_mon.values, training_set_wen.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_mon.values, training_set_thu.values)[1]
stats.kruskal(training_set_mon.values, training_set_fri.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_mon.values, training_set_sat.values)[1]
stats.kruskal(training_set_mon.values, training_set_sun.values)[1]

stats.kruskal(training_set_tue.values, training_set_wen.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_tue.values, training_set_thu.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_tue.values, training_set_fri.values)[1]
stats.kruskal(training_set_tue.values, training_set_sat.values)[1]
stats.kruskal(training_set_tue.values, training_set_sun.values)[1]

stats.kruskal(training_set_wen.values, training_set_thu.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_wen.values, training_set_fri.values)[1]
stats.kruskal(training_set_wen.values, training_set_sat.values)[1]
stats.kruskal(training_set_wen.values, training_set_sun.values)[1]

stats.kruskal(training_set_thu.values, training_set_fri.values)[1]
stats.kruskal(training_set_thu.values, training_set_sat.values)[1]
stats.kruskal(training_set_thu.values, training_set_sun.values)[1]

stats.kruskal(training_set_fri.values, training_set_sat.values)[1]
stats.kruskal(training_set_fri.values, training_set_sun.values)[1]

stats.kruskal(training_set_sat.values, training_set_sun.values)[1]

# MOIS DE L ANNEE
training_set_jan = training_set[training_set.month == 1].visitors_pool_total.dropna(how='any')
training_set_feb = training_set[training_set.month == 2].visitors_pool_total.dropna(how='any')
training_set_mar = training_set[training_set.month == 3].visitors_pool_total.dropna(how='any')
training_set_apr = training_set[training_set.month == 4].visitors_pool_total.dropna(how='any')
training_set_may = training_set[training_set.month == 5].visitors_pool_total.dropna(how='any')
training_set_jun = training_set[training_set.month == 6].visitors_pool_total.dropna(how='any')
training_set_jul = training_set[training_set.month == 7].visitors_pool_total.dropna(how='any')
training_set_aug = training_set[training_set.month == 8].visitors_pool_total.dropna(how='any')
training_set_sep = training_set[training_set.month == 9].visitors_pool_total.dropna(how='any')
training_set_oct = training_set[training_set.month == 10].visitors_pool_total.dropna(how='any')
training_set_nov = training_set[training_set.month == 11].visitors_pool_total.dropna(how='any')
training_set_dec = training_set[training_set.month == 12].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_jan.values, training_set_feb.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_jan.values, training_set_mar.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_jan.values, training_set_apr.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_jan.values, training_set_may.values)[1]
stats.kruskal(training_set_jan.values, training_set_jun.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_jan.values, training_set_jul.values)[1]
stats.kruskal(training_set_jan.values, training_set_aug.values)[1]
stats.kruskal(training_set_jan.values, training_set_sep.values)[1]
stats.kruskal(training_set_jan.values, training_set_oct.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_jan.values, training_set_nov.values)[1]
stats.kruskal(training_set_jan.values, training_set_dec.values)[1]

stats.kruskal(training_set_feb.values, training_set_mar.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_feb.values, training_set_apr.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_feb.values, training_set_may.values)[1]
stats.kruskal(training_set_feb.values, training_set_jun.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_feb.values, training_set_jul.values)[1]
stats.kruskal(training_set_feb.values, training_set_aug.values)[1]
stats.kruskal(training_set_feb.values, training_set_sep.values)[1]
stats.kruskal(training_set_feb.values, training_set_oct.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_feb.values, training_set_nov.values)[1]
stats.kruskal(training_set_feb.values, training_set_dec.values)[1]

stats.kruskal(training_set_mar.values, training_set_apr.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_mar.values, training_set_may.values)[1]
stats.kruskal(training_set_mar.values, training_set_jun.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_mar.values, training_set_jul.values)[1]
stats.kruskal(training_set_mar.values, training_set_aug.values)[1]
stats.kruskal(training_set_mar.values, training_set_sep.values)[1]
stats.kruskal(training_set_mar.values, training_set_oct.values)[1]
stats.kruskal(training_set_mar.values, training_set_nov.values)[1]
stats.kruskal(training_set_mar.values, training_set_dec.values)[1]

stats.kruskal(training_set_apr.values, training_set_may.values)[1]
stats.kruskal(training_set_apr.values, training_set_jun.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_apr.values, training_set_jul.values)[1]
stats.kruskal(training_set_apr.values, training_set_aug.values)[1]
stats.kruskal(training_set_apr.values, training_set_sep.values)[1]
stats.kruskal(training_set_apr.values, training_set_oct.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_apr.values, training_set_nov.values)[1] 
stats.kruskal(training_set_apr.values, training_set_dec.values)[1]

stats.kruskal(training_set_may.values, training_set_jun.values)[1]
stats.kruskal(training_set_may.values, training_set_jul.values)[1]
stats.kruskal(training_set_may.values, training_set_aug.values)[1]
stats.kruskal(training_set_may.values, training_set_sep.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_may.values, training_set_oct.values)[1]
stats.kruskal(training_set_may.values, training_set_nov.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_may.values, training_set_dec.values)[1]

stats.kruskal(training_set_jun.values, training_set_jul.values)[1]
stats.kruskal(training_set_jun.values, training_set_aug.values)[1]
stats.kruskal(training_set_jun.values, training_set_sep.values)[1]
stats.kruskal(training_set_jun.values, training_set_oct.values)[1]
stats.kruskal(training_set_jun.values, training_set_nov.values)[1]
stats.kruskal(training_set_jun.values, training_set_dec.values)[1]

stats.kruskal(training_set_jul.values, training_set_aug.values)[1]
stats.kruskal(training_set_jul.values, training_set_sep.values)[1]
stats.kruskal(training_set_jul.values, training_set_oct.values)[1]
stats.kruskal(training_set_jul.values, training_set_nov.values)[1]
stats.kruskal(training_set_jul.values, training_set_dec.values)[1]

stats.kruskal(training_set_aug.values, training_set_sep.values)[1]
stats.kruskal(training_set_aug.values, training_set_oct.values)[1]
stats.kruskal(training_set_aug.values, training_set_nov.values)[1]
stats.kruskal(training_set_aug.values, training_set_dec.values)[1]

stats.kruskal(training_set_sep.values, training_set_aug.values)[1]
stats.kruskal(training_set_sep.values, training_set_nov.values)[1]
stats.kruskal(training_set_sep.values, training_set_dec.values)[1]

stats.kruskal(training_set_oct.values, training_set_nov.values)[1]
stats.kruskal(training_set_oct.values, training_set_dec.values)[1]

stats.kruskal(training_set_nov.values, training_set_dec.values)[1]

# BASSINS OUVERTS
training_set_sportbad_open = training_set[training_set.sportbad_closed == 0].visitors_pool_total.dropna(how='any')
training_set_sportbad_closed = training_set[training_set.sportbad_closed == 1].visitors_pool_total.dropna(how='any')
stats.kruskal(training_set_sportbad_open.values, training_set_sportbad_closed.values)[1]

training_set_freizeitbad_open = training_set[training_set.freizeitbad_closed == 0].visitors_pool_total.dropna(how='any')
training_set_freizeitbad_closed = training_set[training_set.freizeitbad_closed == 1].visitors_pool_total.dropna(how='any')
stats.kruskal(training_set_freizeitbad_open.values, training_set_freizeitbad_closed.values)[1]

training_set_sauna_open = training_set[training_set.sauna_closed == 0].visitors_pool_total.dropna(how='any')
training_set_sauna_closed = training_set[training_set.sauna_closed == 1].visitors_pool_total.dropna(how='any')
stats.kruskal(training_set_sauna_open.values, training_set_sauna_closed.values)[1]

training_set_kursbecken_open = training_set[training_set.kursbecken_closed == 0].visitors_pool_total.dropna(how='any')
training_set_kursbecken_closed = training_set[training_set.kursbecken_closed == 1].visitors_pool_total.dropna(how='any')
stats.kruskal(training_set_kursbecken_open.values, training_set_kursbecken_closed.values)[1]

# VACANCES
training_set_h0 = training_set[training_set.school_holiday == 0].visitors_pool_total.dropna(how='any')
training_set_h1 = training_set[training_set.school_holiday == 1].visitors_pool_total.dropna(how='any')
training_set_h2 = training_set[training_set.school_holiday == 2].visitors_pool_total.dropna(how='any')
training_set_h3 = training_set[training_set.school_holiday == 3].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_h0.values, training_set_h1.values)[1]
stats.kruskal(training_set_h0.values, training_set_h2.values)[1]
stats.kruskal(training_set_h0.values, training_set_h3.values)[1]

stats.kruskal(training_set_h1.values, training_set_h2.values)[1]
stats.kruskal(training_set_h1.values, training_set_h3.values)[1]

stats.kruskal(training_set_h2.values, training_set_h3.values)[1]

# JOURS FERIES
training_set_b0 = training_set[training_set.bank_holiday == 0].visitors_pool_total.dropna(how='any')
training_set_b1 = training_set[training_set.bank_holiday == 1].visitors_pool_total.dropna(how='any')
training_set_b2 = training_set[training_set.bank_holiday == 2].visitors_pool_total.dropna(how='any')
training_set_b3 = training_set[training_set.bank_holiday == 3].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_b0.values, training_set_b1.values)[1] # nan
stats.kruskal(training_set_b0.values, training_set_b2.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_b0.values, training_set_b3.values)[1] 

stats.kruskal(training_set_b1.values, training_set_b2.values)[1] # nan
stats.kruskal(training_set_b1.values, training_set_b3.values)[1] # nan

stats.kruskal(training_set_b2.values, training_set_b3.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups

# EVENEMENT
training_set_no_event = training_set[(training_set.event == 0) & (training_set.day.isin(['0', '1', '2', '3', '4']))].visitors_pool_total.dropna(how='any')
training_set_event = training_set[(training_set.event == 1) & (training_set.day.isin(['0', '1', '2', '3', '4']))].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_no_event.values, training_set_event.values)[1]

# TOBOGGAN
training_set_no_toboggan = training_set[training_set.sloop_dummy == 0].visitors_pool_total.dropna(how='any')
training_set_toboggan = training_set[training_set.sloop_dummy > 0].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_no_toboggan.values, training_set_toboggan.values)[1] 

# PRIX
training_set_P1 = training_set[training_set.Price == 'P1'].visitors_pool_total.dropna(how='any')
training_set_P2 = training_set[training_set.Price == 'P2'].visitors_pool_total.dropna(how='any')
training_set_P3 = training_set[training_set.Price == 'P3'].visitors_pool_total.dropna(how='any')
training_set_P4 = training_set[training_set.Price == 'P4'].visitors_pool_total.dropna(how='any')
training_set_P5 = training_set[training_set.Price == 'P5'].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_P1.values, training_set_P2.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_P1.values, training_set_P3.values)[1]
stats.kruskal(training_set_P1.values, training_set_P4.values)[1] # nan
stats.kruskal(training_set_P1.values, training_set_P5.values)[1]

stats.kruskal(training_set_P2.values, training_set_P3.values)[1]
stats.kruskal(training_set_P2.values, training_set_P4.values)[1] # nan
stats.kruskal(training_set_P2.values, training_set_P5.values)[1]

stats.kruskal(training_set_P3.values, training_set_P4.values)[1] # nan
stats.kruskal(training_set_P3.values, training_set_P5.values)[1]

stats.kruskal(training_set_P4.values, training_set_P5.values)[1] # nan

# TEMPERATURE
# pas possible

# VITESSE DU VENT
training_set_w0 = training_set[training_set.wind_speed_max == 0].visitors_pool_total.dropna(how='any')
training_set_w1 = training_set[training_set.wind_speed_max == 1].visitors_pool_total.dropna(how='any')
training_set_w2 = training_set[training_set.wind_speed_max == 2].visitors_pool_total.dropna(how='any')
training_set_w3 = training_set[training_set.wind_speed_max == 3].visitors_pool_total.dropna(how='any')
training_set_w4 = training_set[training_set.wind_speed_max == 4].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_w0.values, training_set_w1.values)[1] # nan
stats.kruskal(training_set_w0.values, training_set_w2.values)[1] # nan
stats.kruskal(training_set_w0.values, training_set_w3.values)[1] # nan
stats.kruskal(training_set_w0.values, training_set_w4.values)[1] # nan

stats.kruskal(training_set_w1.values, training_set_w2.values)[1] 
stats.kruskal(training_set_w1.values, training_set_w3.values)[1] 
stats.kruskal(training_set_w1.values, training_set_w4.values)[1] 

stats.kruskal(training_set_w2.values, training_set_w3.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_w2.values, training_set_w4.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups

stats.kruskal(training_set_w3.values, training_set_w4.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups

# PRECIPITATION
training_set_p0 = training_set[training_set.precipitation == 'P0'].visitors_pool_total.dropna(how='any')
training_set_p1 = training_set[training_set.precipitation == 'P1'].visitors_pool_total.dropna(how='any')
training_set_p2 = training_set[training_set.precipitation == 'P2'].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_p0.values, training_set_p1.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups
stats.kruskal(training_set_p0.values, training_set_p2.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups

stats.kruskal(training_set_p1.values, training_set_p2.values)[1] # > 0.05 Accept NULL hypothesis - No significant difference between groups

# SOLEIL
training_set_rs0 = training_set[training_set.sunshine_radiation == 'RS0'].visitors_pool_total.dropna(how='any')
training_set_rs1 = training_set[training_set.sunshine_radiation == 'RS1'].visitors_pool_total.dropna(how='any')
training_set_rs2 = training_set[training_set.sunshine_radiation == 'RS2'].visitors_pool_total.dropna(how='any')
training_set_rs3 = training_set[training_set.sunshine_radiation == 'RS3'].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_rs0.values, training_set_rs1.values)[1] 
stats.kruskal(training_set_rs0.values, training_set_rs2.values)[1] 
stats.kruskal(training_set_rs0.values, training_set_rs3.values)[1] 

stats.kruskal(training_set_rs1.values, training_set_rs2.values)[1]
stats.kruskal(training_set_rs1.values, training_set_rs3.values)[1] 

stats.kruskal(training_set_rs2.values, training_set_rs3.values)[1]

# NEIGE
training_set_no_snow = training_set[(training_set.snow_height == 'S0') & (training_set.month.isin(['12', '1', '2', '3']))].visitors_pool_total.dropna(how='any')
training_set_snow = training_set[(training_set.snow_height == 'S1') & (training_set.month.isin(['12', '1', '2', '3']))].visitors_pool_total.dropna(how='any')

stats.kruskal(training_set_snow.values, training_set_no_snow.values)[1]

#======================================================
# tests sur la correaltion des variables / nb visiteurs
#======================================================
import seaborn as sns
from scipy import stats
from matplotlib import pyplot as plt

stats.pearsonr(training_set.visitors_pool_total.values.astype(int), training_set.temperature.values.astype(int))

corr = training_set[['visitors_pool_total', 'temperature', 'precipitation', 'wind_speed_max']].corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True)

training_set[['visitors_pool_total', 'wind_speed_max']].plot()

ax1 = plt.subplot()
ax1.scatter(training_set.wind_speed_max.values, training_set.visitors_pool_total.values, s=1)
ax1.set_xlim([0, 40])

training_set['day'] =  pd.to_datetime(training_set.date, format='%Y/%m/%d').apply(lambda x: x.day)
plt.plot(training_set[(training_set.year == 2012) & (training_set.month == 1)].day.values, training_set[(training_set.year == 2012) & (training_set.month == 1)].visitors_pool_total.values)

stats.pointbiserialr(training_set.sauna_closed.values.astype(int), training_set.visitors_pool_total.values.astype(int))



