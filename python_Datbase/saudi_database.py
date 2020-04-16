from tweepy import Stream

from textblob_ar.blob import TextBlob
count_positive =0
count_neqative=0
counnt_nurmal=0

import time


import preprocessor as p


import pandas as pd
import tweepy
from tweepy import api, API

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time


#consumer key, consumer secret, access token, access secret.
import tweepy

import time

ACCESS_TOKEN = "915516336469573633-ZlP5DLfzSmUAjq3RDGnJyA5Ij4Z185A"
ACCESS_TOKEN_SECRET = "PcKygIWmIFT07Pl9c3unxkDN4a90oaG6CN1XmFLEpr8bq"
CONSUMER_KEY = "ePdoSD2X5rvz8m3FQBBJxe8P9"
CONSUMER_SECRET = "qdUdgN9nnRzfHp3ybQxSjrnECclYhrh8iuAWxFzY5310j7kbQW"


conn = sqlite3.connect('arab_database3.db')
c = conn.cursor()

def create_table():
    try:
        c.execute(
            "CREATE TABLE IF NOT EXISTS sentiment(id INTEGER PRIMARY KEY AUTOINCREMENT, unix INTEGER, tweet TEXT, sentiment REAL, country TEXT)")
        c.execute("CREATE INDEX fast_id ON sentiment(id)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()

    except Exception as e:
        print(str(e))
create_table()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trend_df_sa = pd.DataFrame()

result_SA = api.trends_place(23424938)

def trending():

    i = 0

    # trend from Saudi Arabia
    print("Trend in Saudi Arabia:")
    for trend in result_SA[0]["trends"][:5]:
        print("\t", trend["name"])
        print(i, end='\r')

        i += 1
        if i == 5:
            break
        else:
            pass



def data_trend():
    # extract tweet from top trend in Saudi Arabia
    i = 0
    for trend in result_SA[0]["trends"][:1]: data = trend["name"]



    print("Top trend is in SA: ", data)






    for tweet in tweepy.Cursor(api.search, q=data + ' -filter:retweets' ,wait_on_rate_limit=True , lang='ar', tweet_mode='extended').items():
        rate_limit=30
        print(i, end='\r')
        p.set_options(p.OPT.URL, p.OPT.EMOJI)
        #print(p.clean(tweet.full_text))


        tweet2=p.clean(tweet.full_text)

        analysis=TextBlob(tweet2)

        sentiment=analysis.sentiment.polarity

        t = tweet.created_at


        country = 'sudi Arabi'
        c.execute("INSERT INTO sentiment (unix, tweet, sentiment,country) VALUES (?, ?, ?,?)",
                  (t, tweet2, sentiment, country))
        conn.commit()







        i += 1
        if i == 1800:
            break
        else:
            time.sleep(2)

            pass



trending()

data_trend()
