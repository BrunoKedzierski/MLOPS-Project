import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = pd.read_csv("mushroom.csv")

#Data loaded properly
data.head()

#There are many missing values in column = "stalk-root"
data.info()




#There are more edible mushrooms but the proportion between edible and poisonous mushrooms is close to one
print(data[['poisonous']].value_counts())






