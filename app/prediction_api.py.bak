from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import wandb
import pickle
from bank_client import Bank_Client
import pyarrow.parquet as pq
import uvicorn
import pandas as pd
from autogluon.tabular import  TabularPredictor



app = FastAPI()
api = wandb.Api()
artifact = api.artifact("asi_grupa_3/bank_dataset/classifier:latest")
model = artifact.download()
loaded_model = pickle.load(open(f'{model}\classifier.pkl', 'rb'))


print(f"Model type: {type(loaded_model)}")

artifact = api.artifact("asi_grupa_3/bank_dataset/encoder:latest")
encoder = artifact.download()
loaded_encoder = pickle.load(open(f'{encoder}\encoder.pkl', 'rb'))


artifact = api.artifact("asi_grupa_3/bank_dataset/train_test_bank_data:latest")
dataset = artifact.download()
df = pq.read_table(source=f'{dataset}\\train_test_bank_data.pq').to_pandas()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/client")
def predict_client(data: Bank_Client):
    data = data.dict()
    dframe = pd.DataFrame(data, index=[0])
    dframe['y'] = 'no'
    dframe[dframe.select_dtypes(include=['object']).columns] = loaded_encoder.transform(dframe.select_dtypes(include=['object']))

    prediction = []
    prob = -1

    prediction =loaded_model.predict(dframe.iloc[:, :-1])
    prob = loaded_model.predict_proba(dframe.iloc[:, :-1])

    # if isinstance(loaded_model, TabularPredictor):
       
    #     prediction =loaded_model.predict(dframe.iloc[:, :-1])
    # else:
    #     prediction = loaded_model.predict(dframe.iloc[:, :-1].values)
    #     prob = loaded_model.predict_proba(dframe.iloc[:, :-1].values)


    
    
    return {
        'prediction': prediction[0],
        'probability':prob
        
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)






