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
access_key = "-"
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
 
def selectUsers(cursor):
	try: 
		selectQuery = ("SELECT DISTINCT twitter_handle, id FROM companies")
		cur = cursor.execute(selectQuery)
		users = list(cursor.fetchall())
		return(users)
	except Exception as ex:
		print(ex)
		   	
#insert tweets into db    	
def insertPost(followers_count, company_id):
	try:
		insertQuery = ("UPDATE companies SET follower_count = %s where id = %s")
		postData = (followers_count, company_id)
		db.cursor().execute(insertQuery, postData)
		db.commit()
	except Exception as ex:
		print(ex)
		
#get last tweets
def get_follower_count(user):
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)
		
		username = api.get_user(str(user[0]))
		userId = user[1]
		followers_count = username.followers_count
		insertPost(followers_count, userId)
		
		print (userId, username.followers_count)	
	except Exception as ex:
		print(ex)		

if __name__ == '__main__':
	try:
		db = connect('', '')
		users = selectUsers(db.cursor())
		for user in users:
			get_follower_count(user)
			
	except Exception as ex: 
		print(ex)
