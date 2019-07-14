import mysql.connector
import config
import requests

dbSelect = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
selectCursor = dbSelect.cursor()
selectQuery = ("SELECT id, twitter_handle FROM companies")
selectCursor.execute(selectQuery)

dbUpdate = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
updateCursor = dbUpdate.cursor()

for (id, twitter_handle) in selectCursor:

    url = "http://www.facebook.com/" + twitter_handle

    print ("Requesting {} ....".format(url))

    response = requests.get(url)

    updateQuery = ("UPDATE companies SET twitter_handle_is_facebook_url = %s WHERE id = %s")

    if response.status_code == 200:
        updateCursor.execute(updateQuery, (1, id))
    else:
        updateCursor.execute(updateQuery, (0, id))

    print (updateCursor.statement)
        
dbSelect.commit()
dbUpdate.commit()
selectCursor.close()
updateCursor.close()
dbSelect.close()
dbUpdate.close()