import pandas as pd

# SVR

training_set = pd.read_csv('data/processed/training_set.csv')
training_set.drop(['Unnamed: 0'], axis=1, inplace=True)

validation_set = pd.read_csv('data/processed/validation_set.csv')
validation_set.drop(['Unnamed: 0'], axis=1, inplace=True)

