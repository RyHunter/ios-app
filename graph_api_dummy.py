import requests
import config
import mysql.connector
        
def getDataFromPost(post):
    message = post['message'].replace('\n', ' ')
    return {
        "id": post['id'],
        "message": message,
        "created_time": post['created_time']
    }

def insertPostData(companyId, message, likesCount, commentsCount, createdTime, cursor):
    insertQuery = ("INSERT INTO posts (company_id, content, likes_count, comments_count, created_time) VALUES (%s, %s, %s, %s, %s)")
    postData = (companyId, message, likesCount, commentsCount, createdTime)
    cursor.execute(insertQuery, postData)

def getCompanyIdByHandle(handle, cursor):
    selectQuery = ("SELECT id FROM companies WHERE twitter_handle=%s")
    cursor.execute(selectQuery, (handle,))
    return cursor.fetchone()[0]

def getHandleByCompanyId(id, cursor):
    selectQuery = ("SELECT twitter_handle FROM companies WHERE id=%s")
    cursor.execute(selectQuery, (id,))
    return cursor.fetchone()[0]

def getAllCompanies(cursor, twitterHandleIsUrl):
    twitterClause = ''
    if twitterHandleIsUrl:
        twitterClause = " WHERE twitter_handle_is_facebook_url"

    selectQuery = ("SELECT id, twitter_handle FROM companies" + twitterClause)
    cursor.execute(selectQuery)
    companiesArray = []
    for result in cursor:
        companiesArray.append({"id": result[0], "handle": result[1]})
    return companiesArray

dbSelect = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
selectCursor = dbSelect.cursor()

dbInsert = mysql.connector.connect(user=config.DATABASE['user'], 
                              password=config.DATABASE['password'],
                              host=config.DATABASE['host'],
                              port=config.DATABASE['port'],
                              database=config.DATABASE['database'])
insertCursor = dbInsert.cursor()

accessToken = config.ACCESS_TOKEN

# for testing only
id = 430
handle = getHandleByCompanyId(id, selectCursor)
companiesArray = [{"id": id, "handle": handle}]

# companiesArray = getAllCompanies(selectCursor, True)
for company in companiesArray:

    nextRequest = "https://graph.facebook.com/v3.3/{}/posts?access_token={}".format(company['handle'], accessToken)

    while nextRequest is not None:

        response = requests.get(nextRequest)
        jsonResponse = response.json()
        print(jsonResponse)
        # exit()
        postsArray = jsonResponse['data']

        for post in postsArray:

            if 'message' in post:
                postData = getDataFromPost(post)
                postId = postData['id']

                # Get likes count for given post
                likesRequest = "https://graph.facebook.com/v3.3/{}/likes?summary=total_count&access_token={}".format(postId, accessToken)
                response = requests.get(likesRequest)
                likesResponse = response.json()
                print(likesResponse)
                # exit()
                likesCount = likesResponse['summary']['total_count'];
                
                # Get comments count for given post
                commentsRequest = "https://graph.facebook.com/v3.3/{}/comments?summary=total_count&access_token={}".format(postId, accessToken)
                response = requests.get(commentsRequest)
                commentsResponse = response.json()
                print(commentsResponse)
                commentsCount = commentsResponse['summary']['total_count'];

                insertPostData(company['id'], postData['message'], likesCount, commentsCount, postData['created_time'], insertCursor)

        nextRequest = None
        if 'paging' in jsonResponse:
            pagingInfo = jsonResponse['paging']
            if 'next' in pagingInfo:
                nextRequest = pagingInfo['next']

dbInsert.commit()
dbSelect.commit()
insertCursor.close()
selectCursor.close()
dbInsert.close()
dbSelect.close()