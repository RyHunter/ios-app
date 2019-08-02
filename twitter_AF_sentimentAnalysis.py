from afinn import Afinn
import mysql.connector

af = Afinn()

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

def selectTweet(cursor):
	try:
		selectQuery  = "SELECT normalized_content, id FROM posts"
		cur = cursor.execute(selectQuery) 
		tweets = cursor.fetchall()
		return (tweets)
	except Exception as ex:
		print(ex)

def getSentiment(tweet, tweet_id):
	try:
		sentiment_score = [af.score(str(tweet))]
		insertQuery = ("UPDATE sentiment SET afinn_sentiment = %s WHERE post_id = %s")
		insertData = (sentiment_score[0], tweet_id)
		db.cursor().execute(insertQuery, insertData)
		db.commit()
		print ("inserted row with " + str(sentiment_score[0]) + " where id is " + str(tweet_id))
	except Exception as ex:
		print(ex)
	
if __name__ == '__main__':
	try:
		db = connect('', '')
		tweets =  selectTweet(db.cursor())	
		for tweet in tweets:
			tweet_id = tweet[1]
			getSentiment(str(tweet[0]), tweet_id)
		
	except Exception as ex: 
		print(ex)
