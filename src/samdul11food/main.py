from typing import Union
from fastapi import FastAPI

import os
from datetime import datetime

app = FastAPI()

@app.get("/")
def idx():
    return {"Hello":"n11", "conn":"ok"}

@app.get("/food")
def food(name:str):
    """
    # 음식 이름 저장 API
    ### 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv

    Args:
     - name(str): 음식 이름

    Return
     - dict, 음식 이름과 저장 시간을 담은 딕셔너리
    """
    save_path=f"{os.path.dirname(os.path.abspath(__file__))}/data"

    os.makedirs(save_path,exist_ok=True)

    dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(f"{save_path}/food.csv","a") as f:
        f.write(f"{name},{dt}\n")

    return {
            "food":name, 
            "time":dt
            }
