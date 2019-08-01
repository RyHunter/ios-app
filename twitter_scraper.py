#!/usr/bin/env python3

import sys
import csv
#fetching tweets
import tweepy
#reading and writing from db
import mysql.connector
import time

#twitter api creds
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#establish database connection 	
def connect(username, password):
	try:
		db = mysql.connector.connect(user=username, 
								  password=password,
								  host='',
								  port= ,
								  database='')
								  							
		return db
	except Exception as ex:
		print(ex)
    	
#insert tweets into db    	
def insertPost(companyId, source, message, likesCount, commentsCount, retweetsCount, createdTime):
	try:
		insertQuery = ("INSERT INTO twitter_posts (company_id, source, content, likes_count, comments_count, retweets_count, created_time) VALUES (%s, %s, %s, %s, %s, %s, %s)")
		postData = (companyId, source, message, likesCount, commentsCount, retweetsCount, createdTime)
		db.cursor().execute(insertQuery, postData)
		db.commit()
	except Exception as ex:
		print(ex)
        	
#get last tweets
def get_tweets(user):
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)
		
		username = user[0]
		userId = user[1]
		source = 'Twitter'
		
		#set tweet count
		number_of_tweets = 5000
		count = 0
		#get tweets
		for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, include_rts = False, tweet_mode="extended").items(number_of_tweets):
		#array of tweet info
			if tweet.in_reply_to_status_id is None:
				ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(str(tweet.created_at),'%Y-%m-%d %H:%M:%S'))
				insertPost(userId, source, tweet.full_text.encode("utf-8"), tweet.favorite_count, 0, tweet.retweet_count, ts)
				count += 1	
			else:
				print("@tweet")	
		print(str(count) + " tweets added for " + str(username))		
	except Exception as ex:
		print(ex)
			
def selectUsers(cursor):
	try: 
		users = []
		data = []
		selectQuery = ("SELECT DISTINCT twitter_handle, id FROM companies")
		cur = cursor.execute(selectQuery)
		users = list(cursor.fetchall())
		return(users)
	except Exception as ex:
		print(ex)
				   	
if __name__ == '__main__':
	try:
		db = connect('username', 'password')
		users = selectUsers(db.cursor())
		for user in users:
			get_tweets(user)
	except Exception as ex: 
		print(ex)
