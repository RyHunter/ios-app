#!/usr/bin/env python3

import sys
import csv
#fetching tweets
import tweepy
#reading and writing from db
import mysql.connector

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
								  port=,
								  database='')
								  							
		return db
	except Exception as ex:
		print(ex)
    	
def insertPost(companyId, source, message, likesCount, commentsCount, retweetsCount, createdTime):
	try:
		insertQuery = ("INSERT INTO posts (company_id, source, content, likes_count, comments_count, retweets_count, created_time) VALUES (%s, %s, %s, %s, %s)")
		postData = (companyId, source, message, likesCount, commentsCount, retweetsCount, createdTime)
		db.cursor().execute(insertQuery, postData)
	except Exception as ex:
		print(ex)
        	
#get last tweets
def get_tweets(username):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#set tweet count
	number_of_tweets = 5
	
	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, include_rts = False, tweet_mode="extended").items(number_of_tweets):
	#array of tweet info
		if tweet.in_reply_to_status_id is None:
			insertPost(screen_name, 'Twitter', tweet.full_text.encode("utf-8"), tweet.favorite_count, 'null', tweet.retweet_count, tweet.created_at)
			#tweets_for_csv.append([username, tweet.created_at, tweet.full_text.encode("utf-8"), tweet.retweet_count, tweet.favorite_count]) 
		
	#outfile = username + "_tweets.csv"
	#print ("writing to " + outfile)
	#with open(outfile, 'w+') as file:
	#		writer = csv.writer(file, delimiter = ',')
	#		writer.writerows(tweets_for_csv) 
			
def selectUsers(cursor):
	try: 
		selectQuery = ("SELECT DISTINCT twitter_handle FROM companies")
		cur = cursor.execute(selectQuery)
		users = list(cursor.fetchall())
		return(users)
	except Exception as ex:
		print(ex)
				   	
if __name__ == '__main__':
	try:
		db = connect('', '')
		users = selectUsers(db.cursor())
		for user in users:
			print (user)
	except Exception as ex: 
		print(ex)
	
	
#	if len(sys.argv) == 2:
#		get_tweets(sys.argv[1])
#	else:
#		print ("error: enter username")
		
		
		
