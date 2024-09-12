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
    음식 이름 저장 API
    # 시간을 저장
    # 음식이름과 시간을 csv로 저장 -> code/data/food.csv

    Args:
     - name(str): 음식 이름

    Return
     - dict, 음식 이름과 저장 시간을 담은 딕셔너리
    """
    
    os.path.expanduser("~")

    time="yyyy-mm-dd hh:mm:ss"
    print(datetime.ctime())

#    with open("~/code/data/food.csv","a") as f:
#        f.write(name,time)

    return {
            "food":name, 
            "time":time
            }
