"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
import pandas
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
import numpy as np
from sdv.single_table import GaussianCopulaSynthesizer

from sdv.lite import SingleTablePreset



def rebalance_data(data):
    rus = RandomUnderSampler(random_state=0)
    X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
    data_undersampled = pd.concat([X_resampled, y_resampled], axis="columns")

    rus = RandomOverSampler(random_state=0)
    X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
    data_oversampled = pd.concat([X_resampled, y_resampled], axis="columns")
    return data_oversampled, data_undersampled


def encode_data(data):
    enc = OrdinalEncoder()
    data[data.select_dtypes(include=['object']).columns] = enc.fit_transform(data.select_dtypes(include=['object']))
    return data, enc


def synthetic(data, rows):
    synthesizer = GaussianCopulaSynthesizer(data.columns)
    synthesizer.fit(data)
    synthetic_data = synthesizer.sample(num_rows=rows)
    return synthetic_data


def preprocess_data(data, rows):
    data = synthetic(data, rows)
    print(data["contact"].unique())
    data, enc = encode_data(data)
    oversampled, undersampled = rebalance_data(data)

    return oversampled, undersampled, enc
