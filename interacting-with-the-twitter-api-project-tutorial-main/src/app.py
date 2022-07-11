import os
import tweepy
import requests
import pandas as pd
from dotenv import load_dotenv
import re

import matplotlib.pyplot as plt
import seaborn as sns

load_dotenv()
consumer_key =  os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets= client.search_recent_tweets(query=query,tweet_fields=['author_id','created_at','lang'],max_results=100)

tweets_dict = tweets.json() 
list(tweets_dict)

tweets_data = tweets_dict['data'] 

df = pd.json_normalize(tweets_data)

df.to_csv("codigo-tweets.csv")

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

[pandas, python] = [0, 0]

for index, row in df.iterrows():
    print(row)
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])

cd = ['pandas', 'python']

ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="Cantidad")
plt.show()