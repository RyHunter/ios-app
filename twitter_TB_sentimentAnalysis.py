import mysql.connector
from textblob import TextBlob

#connect to db
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

def selectTweet(cursor):
	try:
		selectQuery  = "SELECT normalized_content, id FROM posts"
		cur = cursor.execute(selectQuery) 
		tweets = cursor.fetchall()
		return (tweets)
	except Exception as ex:
		print(ex)

def getSentiment(tweet, tweet_id):
	blob = TextBlob(tweet)
	sentiment = blob.sentiment
	polarity = blob.sentiment.polarity
	subjectivity = blob.sentiment.subjectivity
	insertQuery = ("INSERT INTO sentiment (post_id, polarity, subjectivity) VALUES (%s, %s, %s)")
	insertData = (tweet_id, polarity, subjectivity)
	db.cursor().execute(insertQuery, insertData)
	db.commit()
	
if __name__ == '__main__':
	try:
		db = connect('', '')
		tweets =  selectTweet(db.cursor())	
		for tweet in tweets:
			tweet_id = tweet[1]
			getSentiment(str(tweet[0]), tweet_id)
		
	except Exception as ex: 
		print(ex)
