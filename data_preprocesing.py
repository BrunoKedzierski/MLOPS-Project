import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = pd.read_csv("mushroom.csv")


data.drop(columns=['stalk-root'], inplace = True)


enc = OrdinalEncoder()
data_encoded = enc.fit_transform(data)

X = data_encoded[:,0:-1]

y = data_encoded[:,-1]


data_encoded.to_csv("mushroom_preprocessed.csv")


