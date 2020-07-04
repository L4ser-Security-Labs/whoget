#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "15/06/2020"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''OSINT tool  for Nigerian Phone numbers'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

from decouple import config
import requests
import tweepy
import facebook
from bs4 import BeautifulSoup


# Twitter Credentials
TWITTER_API_KEY=config('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY=config('TWITTER_API_SECRET_KEY')
TWITTER_API_ACCESS_TOKEN=config('TWITTER_API_ACCESS_TOKEN')
TWITTER_API_ACCESS_TOKEN_SECRET=config('TWITTER_API_ACCESS_TOKEN_SECRET')

# Facebook Credentials
FACEBOOK_USER_ACCESS_TOKEN=config('FACEBOOK_USER_ACCESS_TOKEN')

#User Agents
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

def twitter(ngnumber):
	"""Twitter search"""
	print ("-" * 30)
	print("[!] Searching Twitter...")
	print ("-" * 30)
	tweets = []
	text_query = ngnumber.replace("+234", "0")
	count = 1000
	auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
	auth.set_access_token(TWITTER_API_ACCESS_TOKEN, TWITTER_API_ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth,wait_on_rate_limit=True)
	try:
		for tweet in api.search(q=text_query, count=count):
			tweets.append((tweet.created_at,tweet.id,tweet.text))
		return tweets
	except BaseException as e:
		print('failed on_status,',str(e))

def fbook(ngnumber):
    """Facebook search"""
    print ("-" * 30)
    print("[!] Searching Facebook...")
    print ("-" * 30)
    graph = facebook.GraphAPI(access_token=FACEBOOK_USER_ACCESS_TOKEN, version = 3.1)
    posts = graph.request('/search?type=place&q=nigeria+{}&fields=id,name,location,link,phone&limit=1000'.format(ngnumber))
    return posts["data"]
