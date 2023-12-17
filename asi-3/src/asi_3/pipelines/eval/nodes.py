"""
This is a boilerplate pipeline 'eval'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from autogluon.tabular import TabularPredictor

import pandas as pd
import logging
import wandb
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    accuracy_score,
    recall_score,
)
import matplotlib.pyplot as plt





def eval_model(model,test):
    X_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]
    y_pred = model.predict(X_test)
    y_probas = model.predict_proba(X_test)
    return y_test, y_pred, y_probas


def log_results(y_test, y_pred, y_probas,parameters, model):
    precision = precision_score(y_pred, y_test)
    accuracy = accuracy_score(y_pred, y_test)
    recall = recall_score(y_pred, y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient Accuracy of %.3f on test data.", accuracy)

    # hyperparameters = dict()
    # hyperparameters = model.get_params()
    # print(hyperparameters)
    # run = wandb.init(project="bank_dataset", config=hyperparameters)

    print("TEST-3")
    run = wandb.init(project="bank_dataset")

    print("TEST-2")
    # wandb.sklearn.plot_roc(y_test, y_probas, y_test.unique())
    wandb.sklearn.plot_feature_importances(model)
    print("TEST-1")
    wandb.sklearn.plot_confusion_matrix(y_test, y_pred, y_test.unique())

    print("TEST0")

    wandb.summary["accuracy"] = accuracy
    wandb.summary["recall"] = recall
    wandb.summary["precision"] = precision


    print("TEST1")
    model_artifact = wandb.Artifact(name='classifier', type='model')
    print("TEST2")
    model_artifact.add_file('data/06_models/classifier_1.pkl', name='classifier.pkl')
    print("TEST3")
    encoder_artifact = wandb.Artifact(name='encoder', type='model')
    print("TEST4")
    encoder_artifact.add_file('data/06_models/encoder_1.pkl', name='encoder.pkl')
    print("TEST5")

    raw_data = wandb.Artifact(name='raw_bank_data', type='dataset')
    print("TEST6")
    raw_data.add_file('data/01_raw/bank_raw.pq')
    print("TEST7")
    train_test_data = wandb.Artifact(name='train_test_bank_data', type='dataset')
    print("TEST8")
    if parameters["rebalance"] == "undersampled":
        train_test_data.add_file('data/02_intermediate/preprocessed_undersampled_bank.pq', name='train_test_bank_data.pq')
        print("TEST9")
    else:
        train_test_data.add_file('data/02_intermediate/preprocessed_oversampled_bank.pq', name='train_test_bank_data.pq')
        print("TEST10")

    print("TEST 11")

    run.log_artifact(raw_data)
    print("TEST 12")
    run.log_artifact(train_test_data)
    print("TEST 13")

    run.log_artifact(model_artifact)
    print("TEST 14")
    run.log_artifact(encoder_artifact)
    print("TEST 15")