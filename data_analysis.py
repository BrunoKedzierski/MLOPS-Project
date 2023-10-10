import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = pd.read_csv("mushroom.csv")

data.head()


data.info()


#There are many missing values in column = "stalk-root"


print(data[['poisonous']].value_counts())

#There are more edible mushrooms but the proportion between edible and poisonous mushrooms is close to one





