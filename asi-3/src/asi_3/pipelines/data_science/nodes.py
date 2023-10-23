"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import logging


def train_test_val_split(data,target_var_name, test_size, val_size):
    X = data.drop([target_var_name], axis=1)
    y = data[[target_var_name]]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y, test_size=test_size)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test,stratify=y_test, test_size=val_size)
    return  X_train, X_test, y_train, y_test,  X_val, y_val



def train_model( X_train, y_train):
    clf = svm.SVC()
    clf.fit(X_train, y_train.values.ravel())
    return clf

def eval_model(model, X_test,y_test):
    score = model.score(X_test, y_test.values.ravel())
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)   