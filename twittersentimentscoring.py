#https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from requests_oauthlib import OAuth1

#Twitter credentials for the app
auth_params = {
    'app_key':'API key',
    'app_secret':'API key',
    'oauth_token':'API key',
    'oauth_token_secret':'API key'
}

# Creating an OAuth Client connection
auth = OAuth1 (
    auth_params['app_key'],
    auth_params['app_secret'],
    auth_params['oauth_token'],
    auth_params['oauth_token_secret']
)

# url according to twitter API
url_rest = "https://api.twitter.com/1.1/search/tweets.json"

# removing retweets and replies to the tweet often uncessary for the analysis
q = '#htz -filter:retweets -filter:replies' # you can change '#htz' to any other tags

# count : no of tweets to be retrieved per one call and parameters according to twitter API
params = {'q': q, 'count': 100, 'lang': 'en',  'result_type': 'recent'}
results = requests.get(url_rest, params=params, auth=auth)
tweets = results.json()
messages = [BeautifulSoup(tweet['text'], 'html5lib').get_text() for tweet in tweets['statuses']]

# format the tweets into a dataframe
df = DataFrame(messages,columns=['TweetTxt'])

# Use VADER sentiment scorer to assign scores for each tweet
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

list = []
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    compoundscore = score['compound']
    list.append(compoundscore)
for message in messages:
    sentiment_analyzer_scores(message)


df2 = DataFrame(list, columns=['sentimentscore'])

df3 = pd.concat([df, df2],axis=1)

print(df3)
print("Overall Compound Score")
print(df3['sentimentscore'].mean())