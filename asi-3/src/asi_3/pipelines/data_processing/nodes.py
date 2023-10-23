"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def drop_missing_data(data, col_names):
    for name in col_names:
     try:
        data.drop(columns=[name], inplace = True)
     except pd.errors.InvalidColumnName: 
        print(f'{name} column name not found!')
    return data

def encode_data(data):
    enc = OrdinalEncoder()
    for col in data.select_dtypes(include=['object']).columns:
       data[[col]] = enc.fit_transform(data[[col]] )
    return data


def preprocess_data(data, col_names):
   data = drop_missing_data(data,col_names)
   return encode_data(data)