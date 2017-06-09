import tweepy
from tweepy import OAuthHandler
import os

consumer_key = os.environ['DEPOKOD_TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['DEPOKOD_TWITTER_CONSUMER_SECRET']
access_token = os.environ['DEPOKOD_TWITTER_ACCESS_TOKEN']
access_secret = os.environ['DEPOKOD_TWITTER_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweet = api.user_timeline('elonmusk')[0]
print(tweet.text)
