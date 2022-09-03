import mysql.connector as mysql
import sqlalchemy as db
import datetime

from dotenv import load_dotenv
load_dotenv()

import os
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASSWORD')
# *****************
# 初期設定
# *****************

conn = mysql.connect(
    host="db",
    user=MYSQL_USER,
    passwd=MYSQL_PASS,
    port=3306,
    database="db",
    buffered = True
)

class SQLhandler:
    def select_all(self):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "select * from students"
        # sql = "insert into books values (NULL, "
        cur.execute(sql)
        data = cur.fetchall()
        return data