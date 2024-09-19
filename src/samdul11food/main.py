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

    ##################################################################
    import pymysql.cursors

    # Connect to the database
    connection = pymysql.connect(host=os.getenv("DB_IP","localhost"),
                                user='food',
                                password='1234',
                                database='fooddb',
                                port=os.getenv("DB_PORT","13306"),
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = """
        #     create or replace table foodhistory (
        #         num INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	    #         username varchar(100) NULL COMMENT '입력자 n01, n02 ....',
	    #         foodname varchar(100) NULL COMMENT '음식이름',
	    #         dt varchar(100) NULL COMMENT '입력시간 예: 2024-09-15 11:12:13'
        #     )
        #     """
        #     cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            # cursor.execute(sql, ('webmaster@python.org',))
            sql = "INSERT INTO `foodhistory`(username, foodname, dt) VALUES (%s, %s, %s)"
            cursor.execute(sql,("n11",name,dt))

            sql = "SELECT * FROM `foodhistory` ORDER BY num DESC LIMIT 1"
            cursor.execute(sql,)
            
            result = cursor.fetchone()
            print(result)
        connection.commit()

        #with connection.cursor() as cursor:
            # Read a single record
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            # cursor.execute(sql, ('webmaster@python.org',))
        #    sql = "SELECT * FROM `foodhistory`"
        #    cursor.execute(sql)
        #    result = cursor.fetchone()
        #    print(result)
    ##################################################################

    return {
            "food":name, 
            "time":dt
            }
