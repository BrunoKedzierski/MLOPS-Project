from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import pickle


def train_model( data,target_var_name,):
    X = data.drop([target_var_name], axis=1)
    y = data[[target_var_name]]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y, test_size=0.25)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test,stratify=y_test, test_size=0.25)
    
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    
    print(clf.score(X_test, y_test))
    filename = 'SVM_Model.pkl'
    pickle.dump(clf, open(filename, 'wb'))
    return clf