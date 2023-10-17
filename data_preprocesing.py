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
    data_encoded = enc.fit_transform(data)
    return data


# X = data_encoded[:,0:-1]
# y = data_encoded[:,-1]
# pd.DataFrame(data_encoded).to_csv("mushroom_preprocessed.csv")


