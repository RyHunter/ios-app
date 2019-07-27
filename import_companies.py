import csv
import mysql.connector
import config

db = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
cursor = db.cursor()

insertQuery = ("INSERT INTO companies (url, name, twitter_handle) VALUES (%s, %s, %s)")

file = open('Fortune-1000-Company-Twitter-Accounts.csv')

companyAccountInfoCsv = csv.DictReader(file)

for row in companyAccountInfoCsv:
    url = row['domain']
    name = row['name']
    twitter_handle = row['twitter']

    companyData = (url, name, twitter_handle)
    cursor.execute(insertQuery, companyData)

db.commit()
cursor.close()
db.close()