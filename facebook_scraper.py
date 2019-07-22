import mysql.connector
import config
import requests
from bs4 import BeautifulSoup

db = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
cursor = db.cursor()

selectQuery = ("SELECT id, twitter_handle FROM companies")

cursor.execute(selectQuery)

for (id, twitter_handle) in cursor:

    url = "http://www.facebook.com/" + twitter_handle

    print ("Requesting {} ....".format(url))

    response = requests.get(url)

    print (response.content)

    # if response.status_code == 404:
    #     print(url + " not found")
    #     continue

    # print (response.text)