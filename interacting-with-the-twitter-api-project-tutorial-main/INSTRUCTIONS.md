# Interacting with the Twitter API

Twitter can be used as a data source for various data science projects.

In this exercise we will learn how to interact with the Twitter API. We will practice storing tweets in a dataframe and saving them into a csv file.

Tweepy is a Python library to access the Twitter API. You’ll need to set up a twitter application at dev.twitter.com to obtain a set of authentication keys to use with the API. 

### Step 1: Create a twitter developer account

Create an App in the developer account: https://developer.twitter.com/ . 

Make sure to get the bearer_token, consumer_key, consumer_secret, access_token, access_token_secret and have them in a safe place.
These can be generated in your developer portal, under the “Keys and tokens” tab for your developer App.

Guidance on how to create a Twitter app (step 1 and 2): https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2

### Step 2: Initial setup

- Create an app.py file inside the `./src/` folder. 
- Install tweepy using PIP.

### Step 3: Environment variables

You need to provide the Twitter keys and tokens in order to use the API v2.

To do it in a safe way, you should store the secrets in a seperate .env file.
A dotenv file contains only text, where it has one environment variable assignment per line.
Create a .env file in your project and add your secret keys or passwords: 

```py
CONSUMER_KEY="insert your API key"
CONSUMER_SECRET="insert your API secret"
ACCEESS_TOKEN="insert your access token"
ACCESS_TOKEN_SECRET="insert your access token secret"
BEARER_TOKEN="insert your bearer token"
```

> Important: Make sure to add the .env inside your .gitignore file, which is not saved to source control, so that you aren't putting potentially sensitive information at risk. 

Now, you need to install python-dotenvpackage. python-dotenv is a Python package that lets your Python app read a .env file. This package will search for a .env and if it finds one, will expose the variables in it to the app.

Example:

```py
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    

import os 

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

```

To set password or secret keys in environment variable on Linux(and Mac) or Windows, see the following link: https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0

### Step 4: Innitialize the tweepy library

- Import Tweepy and [requests library](https://requests.readthedocs.io/en/latest/)
- Make a connection with API v2. Use the variables in the function `tweepy.Client()`. 

> Use the following documentation for guidance on the parameters: https://docs.tweepy.org/en/stable/client.html

### Step 5: Start making requests to the API

- Make a query: Search tweets that have the hashtag #100daysofcode and the word python or pandas, from the last 7 days (search_recent_tweets). 
- Do not include retweets. Limit the result to a maximum of 100 Tweets.
- Also include some additional information with tweet_fields (author id, when the tweet was created, the language of the tweet text).

You can use this link for guidance on how to create the query: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query


1. Define query
2. Get a max. 100 tweets (it's the max allowed by the twitter API)
```

### Step 6: Convert to pandas Dataframe

1. import pandas
2. Save data as dictionary
3. Extract "data" value from dictionary
4. Transform to pandas Dataframe
5. Take a look at the dataframe to make sure is correct `df.head()`
6. Save the data as a CSV file named coding-tweets.csv


### Step 7: Search for the words

Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 'pandas', and 'python'. Define the following function word_in_text(), which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet). 

> Make sure to convert any word or tweet text into lowercase.
> You can use the re python library (regular expression operations). See the documentation for guidance: https://docs.python.org/3/library/re.html#


1. import de `re` library using `import re`
2. Define your `word_in_text` function and implement the code.


### Step 11:

Iterate through dataframe rows counting the number of tweets in which pandas and python are mentioned, using your word_in_text() function.

1. Initialize list to store tweet counts
2. Iterate through df, counting the number of tweets in which each(pandas and python) is mentioned.

### Step 12: Visualize the data

1. Import packages
2. Set seaborn style
3. Create a list of labels:cd
4. Plot the bar chart

Source: 

https://www.kirenz.com/post/2021-12-10-twitter-api-v2-tweepy-and-pandas-in-python/twitter-api-v2-tweepy-and-pandas-in-python/

https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query