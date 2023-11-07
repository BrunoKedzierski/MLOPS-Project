"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import logging
import wandb
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score, recall_score
import matplotlib.pyplot as plt


def train_test_val_split(data,parameters):
    X = data[parameters['features']]
    y = data[parameters['target_var_name']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y, test_size=parameters['test_size'], random_state=parameters['random_state'])
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test,stratify=y_test, test_size=parameters['val_size'], random_state=parameters['random_state'])
    return  X_train, X_test, y_train, y_test,  X_val, y_val



def train_model( X_train, y_train, parameters):
    clf = svm.SVC( kernel=parameters['kernel'], random_state=parameters['random_state'])
    clf.fit(X_train, y_train.values.ravel())
    return clf

def eval_model(model, X_test,y_test,parameters):
    
    y_pred = model.predict(X_test)
    precision = precision_score(y_pred, y_test)
    accuracy = accuracy_score(y_pred, y_test)
    recall = recall_score(y_pred, y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient Accuracy of %.3f on test data.", accuracy)   

    run = wandb.init(project="visualize-sklearn", config=parameters)
    

    # Calculate confusion matrix
    confusion_mat = confusion_matrix(y_test, y_pred)

    # Log confusion matrix as an artifact
    plt.figure()
    wandb.sklearn.plot_confusion_matrix(y_true=y_test, y_pred=y_pred, labels=model.classes_)
    confusion_matrix_plot = plt.gcf()
    wandb.log({"confusion_matrix": wandb.Image(confusion_matrix_plot)})

    wandb.summary["accuracy"] = accuracy
    wandb.summary["recall"] = recall
    wandb.summary["precision"] = precision

    run.log_code()