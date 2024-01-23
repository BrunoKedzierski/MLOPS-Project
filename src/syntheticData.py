from sdv.single_table import GaussianCopulaSynthesizer

import pandas as pd
import numpy as np
from numpy import random




data_job = ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                        'services', 'self-employed', 'unemployed', 'housemaid', 'student']

data_marital = ['married', 'single', 'divorced']
data_education = ['tertiary', 'secondary', 'primary']
data_default =["yes", "no"]
data_housing = ["yes", "no"]
data_contact = ["cellular", "telephone"]
data_loan = ["yes", "no"]
data_month = ["january", "february", "march", "april", "may", "june", "july","august", "september", "october", "november", "necember"][:3]
data_y = ["yes", "no"]

job=[]
marital=[]
education=[]
default=[]
housing=[]
contact=[]
loan=[]
month=[]

age=[]
balance=[]
day_of_week=[]
duration=[]
campaign=[]
pdays=[]
previous=[]
y=[]



for x in range(10000):
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
    balance.append(np.random.randint(-8019,102127))
    day_of_week.append(np.random.randint(1,31))
    duration.append(np.random.randint(0,4918))
    campaign.append(np.random.randint(1,63))
    pdays.append(np.random.randint(-1,873))
    previous.append(np.random.randint(0,275))


df = pd.DataFrame(zip(age,job,marital,education,default,balance,housing,loan,contact,day_of_week,month,duration,campaign,pdays,previous,y),columns=['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
       'loan', 'contact', 'day_of_week', 'month', 'duration', 'campaign',
       'pdays', 'previous', 'y'])
print(df)



gaussian_model = GaussianCopulaSynthesizer()
gaussian_model.fit(df.iloc[:1000])


