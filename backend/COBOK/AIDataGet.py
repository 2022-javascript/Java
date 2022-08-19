import requests
import pymysql
import base64
import sys
from dataread import *
from datetime import datetime
host = "ai-predict.cyyrt9e5hsme.ap-northeast-2.rds.amazonaws.com"
port = 3306
username = "admin"
database = "AI_predict"
password = "825582qaz"
today_datetime = datetime.today().strftime("%Y-%m-%d") # YYYY-mm-dd 형태의 시간 출력
ticker = download_data().Usdt_symbol()
def connect_RDS(host,port,username,password,database):
    conn = pymysql.connect(host = host,user = username, passwd=password, db=database,
    port=port, use_unicode = True, charset='utf8')
    return conn
def res_data():
    dic = {}
    for i in ticker:
            # 데이터 검색 
            conn = connect_RDS(host,port,username,password,database)
            cursor = conn.cursor()

            sql = "SELECT * FROM "+ str(i).replace("/","_")+ " where date = " + '"' + str(today_datetime) + '"'
            cursor.execute(sql) 
            res = cursor.fetchall()
            dic[str(i).replace("/","_")] = res[0][1]
            conn.commit() 
            conn.close()
    return dic