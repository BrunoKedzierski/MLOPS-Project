from typing import Union
from fastapi import FastAPI
import wandb
import pickle
from bank_client import Bank_Client
import pyarrow.parquet as pq
import uvicorn
import pandas as pd
from autogluon.tabular import  TabularPredictor







app = FastAPI()
api = wandb.Api()
model_artifact = api.artifact("asi_grupa_3/bank_dataset/classifier:latest")
encoder_artifact = api.artifact("asi_grupa_3/bank_dataset/encoder:latest")
model = model_artifact.download()
loaded_model = pickle.load(open(f'{model}\classifier.pkl', 'rb'))

encoder = encoder_artifact.download()
loaded_encoder = pickle.load(open(f'{encoder}\encoder.pkl', 'rb'))









@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/downloadmodels")
def read_root():
    global loaded_model, loaded_encoder
    model =  model_artifact.download()
    loaded_model = pickle.load(open(f'{model}\classifier.pkl', 'rb'))
    
    encoder =  encoder_artifact.download()
    loaded_encoder =  pickle.load(open(f'{encoder}\encoder.pkl', 'rb'))


@app.get("/modelinfo")
def show_model_info():
    return {"model_ver": model_artifact.version,
            "model_name": model_artifact.name,
            "model_type": type(loaded_model).__name__,
            "model_meta": model_artifact.metadata}


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



    
    
    return {
        'prediction': prediction[0],
        'probabilityA': prob[0][0],
        'probabilityB': prob[0][1]
        
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)






