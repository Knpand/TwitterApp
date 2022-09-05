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
REPLY_TO_ACCOUNT    = os.getenv("REPLY_TO_ACCOUNT")
print(CONSUMER_KEY)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_TOKEN)
auth.set_access_token(ACCESS_KEY, ACCESS_TOKEN)
api = tweepy.API(auth)

# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = os.getenv("BEARER_TOKEN_GIRL"),
                           consumer_key    = os.getenv("API_KEY_GIRL"),
                           consumer_secret = os.getenv("API_SECRET_GIRL"),
                           access_token    =os.getenv("ACCESS_TOKEN_GIRL"),
                           access_token_secret =  os.getenv("ACCESS_TOKEN_SECRET_GIRLT"),
                          )
    return client


def autoreply():
    new_tweet_ID=""
    client=ClientInfo()
    id = REPLY_TO_ACCOUNT 
    while True:
        try:
            time.sleep(10)
            tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])

            for tweet in tweets.data:
                print(tweet.text)
                if(tweet.text[0]=='@'):
                    continue
                else:
                    if new_tweet_ID != tweet.id:
                        print("new tweet")
                        new_tweet_ID=tweet.id
                        response = requests.post('https://chatbot-api.userlocal.jp/api/chat', data={'key': CHATBOTKEY_GIRL,'message':tweet.text}).text
                        stud_obj = json.loads(response)
                        response = requests.post('https://chatbot-api.userlocal.jp/api/character', data={'key': CHATBOTKEY_GIRL,'message':stud_obj['result'],'character_type':"cat"}).text
                        stud_obj = json.loads(response)
                        response = client.create_tweet(text=stud_obj, in_reply_to_tweet_id=new_tweet_ID)
                    else:
                        print("existed tweet")
                    break
        except:
            print("catAPI 1 error")
            import traceback
            traceback.print_exc()


        try:
      
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
            import traceback
            traceback.print_exc()
            print("cat api 2 error")

     
        



