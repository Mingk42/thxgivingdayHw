from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from datetime import datetime, timezone, timedelta

app = FastAPI()

origins = [
    "http://localhost",
    "https://samdul11food.web.app",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origin_regex=f"http://localhost[:\d]*",
    allow_origins=origins,
    allow_origin_regex=f"{origins[0]}[:\d]*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    
    KST = timezone(timedelta(hours=9))
    dt=datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')

    with open(f"{save_path}/food.csv","a") as f:
        f.write(f"{dt},{name}\n")

    return {
            "food":name, 
            "time":dt
            }
