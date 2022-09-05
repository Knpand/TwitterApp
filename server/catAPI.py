import tweepy
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import time 
from catsql import SQLhandler
sqlhandler = SQLhandler()


# ここに取得したキーを書く
CONSUMER_KEY = os.getenv("API_KEY_GIRL")
CONSUMER_TOKEN = os.getenv("API_SECRET_GIRL")
ACCESS_KEY = os.getenv("ACCESS_TOKEN_GIRL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN_SECRET_GIRL")
CHATBOTKEY_GIRL  = os.getenv("CHATBOTKEY")
print(CONSUMER_KEY)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_TOKEN)
auth.set_access_token(ACCESS_KEY, ACCESS_TOKEN)
api = tweepy.API(auth)



def autoreply():
    while True:
        try:
            time.sleep(60)
            results=api.mentions_timeline()
            for res in results:
                print(res.text)
                print(res.id)
                db_replydata=sqlhandler.select_tweet(res.id)
                
                if len(db_replydata) == 0:
                    response = requests.post('https://chatbot-api.userlocal.jp/api/chat', data={'key': CHATBOTKEY_GIRL,'message':res.text}).text
                    stud_obj = json.loads(response)
                    response = requests.post('https://chatbot-api.userlocal.jp/api/character', data={'key': CHATBOTKEY_GIRL,'message':stud_obj['result'],'character_type':"cat"}).text
                    stud_obj = json.loads(response)
                    print(stud_obj["result"])
                    mes="@"+res.author.screen_name+"\n"
                    mes=mes+stud_obj["result"]
                    api.update_status(mes,in_reply_to_status_id = res.id)
                    sqlhandler.insert_tweetID(res.id)
                else:
                    print("done reply")
        except:
            print("cat api error")


