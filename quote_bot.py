from random import randint
from random import seed
import json
import sys
import tweepy
from os import environ

seed()
rand = randint(0, 364) #change the 2nd number to max number of quotes - 1

consumer_key = 'API_KEY'
consumer_secret_key = "API_SECRET"
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

file = open('example.json')
database = json.load(file)

getText = database[rand]
getEntry = database[rand]

text = getText['text']
entry = getEntry['author']



def createTweet():
    tweet = (f' \"{text}\" \n-{entry}')
    return tweet




def tweet_quote():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    test_tweet = createTweet()
    api.update_status(test_tweet)

if __name__ == "__main__":
    tweet_quote()