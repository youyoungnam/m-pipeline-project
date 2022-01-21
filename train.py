import logging
from random import random 
import pandas as pd
import os 
import joblib
from pathlib import Path 
from joblib import dump
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor


logger = logging.getLogger(__name__)
def prepare_dataset(test_size = 0.2, random_seed=1):
    datasets = pd.read_csv(
        "winequality-red.csv",
        delimiter=','
    )
    datasets = datasets.rename(columns=lambda x: x.lower().replace(" ", "_"))
    y = datasets["quality"]
    datasets = datasets.drop("quality", axis=1)

    train_x, test_x, train_y, test_y = train_test_split(datasets, y,test_size=test_size, random_state=random_seed)
    return {
        "train_x" : train_x,
        "train_y" : train_y,
        "test_x" : test_x,
        "test_y" : test_y
    }

def train():
    logger.info("데이터 셋 불러오는 중입니다...")
    dataset = prepare_dataset()
    train_x = dataset["train_x"]
    train_y = dataset["train_y"]
    test_x = dataset["test_x"]
    test_y = dataset["test_y"]
    train_x = StandardScaler().fit(train_x).transform(train_x)
    test_x = StandardScaler().fit(test_x).transform(test_x)
    print(f"train shape: {train_x.shape}\ntest_shape: {test_x.shape}")

    model = RandomForestRegressor(max_depth=11)
    result = model.fit(train_x, train_y)

    predict = result.predict(test_x)
    error = mean_squared_error(test_y, predict)
    logger.info(f"테스트 데이터 MSE: {error}")

    logger.info("Saving model and artifacts...")
    # Path("artifacts").mkdir(exist_ok=True)

    dump(model, "artifacts/model.joblib")
def predict(model_path = ""):
    data = prepare_dataset()
    test_xx = data["test_x"]
    print(test_xx.iloc[0, :].values.reshape((1, -1)))
    model = joblib.load(model_path)
    print(model.predict(test_xx.iloc[0, :].values.reshape((1, -1))))
    # print(model.predict(test_xx).shape)
if __name__=="__main__":
    logging.basicConfig(level=logging.INFO) 
    if "model.joblib" not in os.listdir('./artifacts'):
        train()
    else:
        predict("./artifacts/model.joblib")
