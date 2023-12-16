"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

def load_data():
    return pd.read_csv("https://archive.ics.uci.edu/static/public/222/data.csv")


def drop_impute_missing_data(data):
   
   columns_to_drop = data.columns[data.isnull().mean() > 0.5]

   
   data = data.drop(columns=columns_to_drop)

   remaining_columns = data.columns[data.isnull().any()]

   categorical_columns = data[remaining_columns].select_dtypes(include='object').columns
   for col in categorical_columns:
      imputer = SimpleImputer(strategy='most_frequent')
      data[col] = imputer.fit_transform(data[[col]])

   numerical_columns = data[remaining_columns].select_dtypes(exclude='object').columns
   for col in numerical_columns:
      imputer = SimpleImputer(strategy='mean')
      data[col] = imputer.fit_transform(data[[col]])
   return data

def rebalance_data(data):
     
          rus = RandomUnderSampler(random_state=0)
          X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
          data_undersampled =  pd.concat([X_resampled, y_resampled], axis="columns")
          
          rus = RandomOverSampler(random_state=0)
          X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
          data_oversampled =  pd.concat([X_resampled, y_resampled], axis="columns")
          return data_oversampled, data_undersampled

def encode_data(data):
    enc = OrdinalEncoder()
    data[data.select_dtypes(include=['object']).columns] = enc.fit_transform(data.select_dtypes(include=['object']))
    return data, enc


def preprocess_data(data):
   data = drop_impute_missing_data(data)
   data,enc = encode_data(data)
   oversampled, undersampled = rebalance_data(data)
   return oversampled, undersampled, enc