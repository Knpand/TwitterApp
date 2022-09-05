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
    host="catdb",
    user=MYSQL_USER,
    passwd=MYSQL_PASS,
    port=3306,
    database="catdb",
    buffered = True
)

class SQLhandler:
    def select_all(self):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "select * from dictionary"
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def select_tweet(self,tweet_id):
        conn.ping(reconnect=True)
        cur = conn.cursor()

        sql = "select * from donereply WHERE tweetID = '"+str(tweet_id)+ "'"
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def insert_tweetID(self,value):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "insert into donereply (tweetID) VALUE ( '"+str(value)+ "' )"
        cur.execute(sql)
        conn.commit()