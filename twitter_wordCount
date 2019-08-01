import spacy
import mysql.connector

nlp = spacy.load('en_core_web_sm')

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

def countWords(tweet, tweet_id):
	try:
		doc = nlp(tweet)
		noun = 0
		pron = 0
		verb = 0
		adj = 0
		adv = 0

		for token in doc:
			tokens = [token.text for token in doc if not token.is_stop]
			if str(token.pos_) == 'NOUN':
				noun += 1
			elif str(token.pos_) == 'PRON':
				pron += 1
			elif str(token.pos_) == 'VERB':
				verb += 1
			elif str(token.pos_) == 'ADJ':
				adj += 1
			elif str(token.pos_) == 'ADV':
				adv += 1	
				
		insertQuery = ("INSERT INTO word_count (post_id, NOUN, PRON, VERB, ADJ, ADV) VALUES (%s, %s, %s, %s, %s, %s)")
		insertData = (tweet_id, noun, pron, verb, adj, adv)
		db.cursor().execute(insertQuery, insertData)
		db.commit()
		print ("inserted row with id ", str(tweet_id))
	except Exception as ex:
		print(ex)
				
if __name__ == '__main__':
	try:
		db = connect('', '')
		tweets =  selectTweet(db.cursor())	
		for tweet in tweets:
			tweet_id = tweet[1]
			countWords(str(tweet[0]), tweet_id)
		
	except Exception as ex: 
		print(ex)
