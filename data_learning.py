from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd


data_encoded =pd.read_csv("mushroom_preprocessed.csv")

print(data_encoded)


X = data_encoded[:,0:-1]

y = data_encoded[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   stratify=y,
                                                    test_size=0.25)


clf = svm.SVC()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

