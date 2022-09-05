import tweepy
from pprint import pprint
# import schedule
import time
import random
from dotenv import load_dotenv
load_dotenv()

import os
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASSWORD')

# API情報を記入
BEARER_TOKEN        = os.getenv("BEARER_TOKEN")
API_KEY             = os.getenv("API_KEY")
API_SECRET          = os.getenv("API_SECRET")
ACCESS_TOKEN        = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
REPLY_TO_ACCOUNT    = os.getenv("REPLY_TO_ACCOUNT")

from sql import SQLhandler
sqlhandler = SQLhandler()
# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    return client



def getsentence():
    data=sqlhandler.select_all()
    sentences  = []
    for i in data:
        print(i[1])
        sentences.append(i)

   
    randint=random.randint(0,len(sentences)-1)
    print(sentences)
    print(randint)
    return sentences[randint][1]


def autoreply():
    new_tweet_ID=""
    client=ClientInfo()

    while True:
        time.sleep(60)
        id = REPLY_TO_ACCOUNT 
        try:
            tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])

            for tweet in tweets.data:
                print(tweet.text)
                if(tweet.text[0]=='@'):
                    continue
                else:
                    if new_tweet_ID != tweet.id:
                        print("new tweet")
                        new_tweet_ID=tweet.id
                        response = client.create_tweet(text=getsentence(), in_reply_to_tweet_id=new_tweet_ID)
                    else:
                        print("existed tweet")
                    break
        except:
            print("twitterAPI error")

# 関数
def CreateTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet

# autoreply()