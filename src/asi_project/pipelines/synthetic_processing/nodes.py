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


def load_data():
    return pd.read_csv("https://archive.ics.uci.edu/static/public/222/data.csv")


def drop_impute_missing_data(data):
    columns_to_drop = data.columns[data.isnull().mean() > 0.5]

    data = data.drop(columns=columns_to_drop)
    data[data == "NaN"] = np.nan
    remaining_columns = data.columns[data.isnull().any()]
    # Separate categorical and numerical columns
    categorical_columns = data[remaining_columns].select_dtypes(include='object').columns
    numerical_columns = data[remaining_columns].select_dtypes(exclude='object').columns
    print(categorical_columns)
    print(numerical_columns)
    # Impute categorical columns
    if not categorical_columns.empty:
        categorical_imputer = SimpleImputer(strategy='most_frequent')
        data[categorical_columns] = categorical_imputer.fit_transform(data[categorical_columns])

    # Impute numerical columns
    if not numerical_columns.empty:
        numerical_imputer = SimpleImputer(strategy='mean')
        data[numerical_columns] = numerical_imputer.fit_transform(data[numerical_columns])

    return data


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


def synthetic():
    data_job = ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                'services', 'self-employed', 'unemployed', 'housemaid', 'student']

    data_marital = ['married', 'single', 'divorced']
    data_education = ['tertiary', 'secondary', 'primary']
    data_default = ["yes", "no"]
    data_housing = ["yes", "no"]
    data_contact = ["cellular", "telephone"]
    data_loan = ["yes", "no"]
    data_month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "necember"][:3]
    data_y = ["yes", "no"]

    job = []
    marital = []
    education = []
    default = []
    housing = []
    contact = []
    loan = []
    month = []

    age = []
    balance = []
    day_of_week = []
    duration = []
    campaign = []
    pdays = []
    previous = []
    y = []

    for x in range(100000):
        job.append(np.random.choice(data_job))
        marital.append((np.random.choice(data_marital)))
        education.append(np.random.choice(data_education))
        default.append(np.random.choice(data_default))
        housing.append(np.random.choice(data_housing))
        contact.append((np.random.choice(data_contact)))
        loan.append(np.random.choice(data_loan))
        month.append(np.random.choice(data_month))
        y.append(np.random.choice(data_y))

        age.append(np.random.randint(0, 100))
        balance.append(np.random.randint(-8019, 102127))
        day_of_week.append(np.random.randint(1, 31))
        duration.append(np.random.randint(0, 4918))
        campaign.append(np.random.randint(1, 63))
        pdays.append(np.random.randint(-1, 873))
        previous.append(np.random.randint(0, 275))

    df = pd.DataFrame(
            zip(age, job, marital, education, default, balance, housing, loan, contact, day_of_week, month, duration,
                campaign, pdays, previous, y),
            columns=['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
                     'loan', 'contact', 'day_of_week', 'month', 'duration', 'campaign',
                     'pdays', 'previous', 'y'])
    return df


def preprocess_data():
    data=synthetic()
    print(data["contact"].unique())
    data = drop_impute_missing_data(data)
    data, enc = encode_data(data)
    oversampled, undersampled = rebalance_data(data)


    return oversampled, undersampled, enc
