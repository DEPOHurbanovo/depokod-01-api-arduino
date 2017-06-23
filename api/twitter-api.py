import tweepy
from tweepy import OAuthHandler
import os
import goslate
import sys

# Morse code translation table
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

consumer_key = os.environ['DEPOKOD_TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['DEPOKOD_TWITTER_CONSUMER_SECRET']
access_token = os.environ['DEPOKOD_TWITTER_ACCESS_TOKEN']
access_secret = os.environ['DEPOKOD_TWITTER_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Access and read the tweet
api = tweepy.API(auth)
tweet = api.user_timeline('chuck_facts')[1]

# Translate the tweet
gs = goslate.Goslate()
translated = gs.translate(tweet.text, 'sk')

api.update_status(translated)

# Translate to morse code
translated_raw = translated
for char in translated_raw:
		print(CODE[char.upper()])
