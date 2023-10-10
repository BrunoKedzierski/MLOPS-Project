from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd


data_encoded =pd.read_csv("mushroom_preprocessed.csv").to_numpy()


X = data_encoded[:,0:-1]

y = data_encoded[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   stratify=y,
                                                    test_size=0.25)
pd.DataFrame(X_train).to_csv("X_train.csv")
pd.DataFrame(X_test).to_csv("X_test.csv")
pd.DataFrame(y_train).to_csv("y_train.csv")
pd.DataFrame(y_test).to_csv("y_test.csv")

clf = svm.SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


