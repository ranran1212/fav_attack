# -*- coding: utf-8 -*-
import tweepy
import time

CONSUMER_KEY = '***'                             # Consumer Key
CONSUMER_SECRET = '***'         # Consumer Secret
ACCESS_TOKEN = '***' # Access Token
ACCESS_SECRET = '***'         # Accesss Token Secert

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def work():
	search_results = api.search(q="@screen_name", count=10)
	for result in search_results:
		tweet_id = result.id
		try:
			api.create_favorite(tweet_id)
		except Exception as e:
			print(e)

while True:
	work()
	interval = 600
	time.sleep(interval)
