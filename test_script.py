#!/usr/bin/python3

import sys
#for connecting to mysql db 
import pymysql
#creating a csv file from db entries
import csv
#credentials from a separate file 
import credentials
#import twython to test the Twitter API 
from twython import Twython
#for reading Twitter credentials
import json

#open database connection
db = pymysql.connect(credentials.address, credentials.username, 
    credentials.password, credentials.db_name)

#create a cursor object 
cursor = db.cursor()

#execute SQL query 
db_data = cursor.execute("SELECT username FROM company_list")

field_name = ["company_handle"]

#create a csv file and populate it with usernames
#that we have stored in our database
with open('companies.json', 'w', newline='') as f_output:
    csv_file = csv.writer(f_output)
    csv_file.writerow(field_name)

    for data in db_data:
        csv_file.writerow(
            [
                data['username'].encode('utf8')
            ]
        )

db.close

#store credentials in a variable
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

#create a test query
query = {'q': 'machine learning',
    'result_type': 'popular',
    'count': 5,
    'lang': 'en',
    }

#creating a search object just to see that 
#my setup is working and all information is correct
#Not doing any scraping yet as we haven't finalized 
#tables and format for that yet
import pandas as pd 

#search some tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['test'])
    dict_['favorite_count'].append(status['favorite_count'])

#structure the data in a dataframe
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

