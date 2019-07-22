import mysql.connector

def connect(username, password):
    db = mysql.connector.connect(user=username, 
                              password=password,
                              host='ios-summer-2019.c7rm7mi2tqkz.us-east-2.rds.amazonaws.com',
                              port=3305,
                              database='ios_summer_2019')
    return db
