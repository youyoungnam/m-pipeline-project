import joblib
import json
from fastapi import FastAPI, Query 
from train import prepare_dataset
from typing import List, Optional
from train import rmse 
app = FastAPI()


@app.get("/prediction")
def predicts():
    data = prepare_dataset()
    test_xx = data['test_x']
    print(test_xx.iloc[0, :].values.reshape((1, -1)))
    model = joblib.load("./artifacts/model.joblib")
    result = model.predict(test_xx.iloc[0, :].values.reshape((1, -1)))
    print(result[0])
    return{
        "checkId":2,
        "predictions": result[0],
        'rmse': rmse
    }