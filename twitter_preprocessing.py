#!/usr/bin/env python3

import mysql.connector
import csv
import string
import re

#connect to db
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
		
def updateTweetContent(cursor):
	try:
		print("begin update...")
		selectQuery  = "SELECT id FROM posts"
		cur = cursor.execute(selectQuery) 
		ids = cursor.fetchall()
		for one in ids:
			print("updating " + str(one))
			selectQuery = ("SELECT content FROM posts WHERE id = %s")
			cur = cursor.execute(selectQuery, one)
			content = cursor.fetchone()
			content = normalizeContent(content)
			insertQuery = ("UPDATE posts SET normalized_content = %s WHERE id = %s")
			insertData = (content, one[0])
			db.cursor().execute(insertQuery, insertData)
			db.commit()
		print("finish update...")
	except Exception as ex:
		print(ex)

def normalizeContent(content):
	try:
		content = re.sub(r'http\S+', '', str(content))
		content = ''.join(i for i in content if not i.isdigit())
		content = removePunctiation(content)	
		content = content.lower()
		return content
	except Exception as ex:
		print(ex)	
					
def removePunctiation(content):
	try:
		print("removing punctuation...")
		table = str.maketrans({key: None for key in string.punctuation})
		content = str(content).translate(table) 
		return (content)
	except Exception as ex:
		print(ex)		

if __name__ == '__main__':
	try:
		db = connect('', '')
		tweet =  updateTweetContent(db.cursor())	
		
	except Exception as ex: 
		print(ex)
