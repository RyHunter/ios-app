def getPost(id, cursor):
    selectQuery = ("SELECT id, company_id, content, likes_count, comments_count, retweets_count, created_time FROM posts WHERE id=%s")
    cursor.execute(selectQuery, (id,))
    post = cursor.fetchone()
    return {
            "id": post[0],
            "company_id": post[1], 
            "content": post[2], 
            "likes_count": post[3], 
            "comments_count": post[4], 
            "retweets_count": post[5], 
            "created_time": post[6]
    }

def getPosts(cursor):
    selectQuery = ("SELECT id, company_id, content, likes_count, comments_count, retweets_count, created_time FROM posts")
    cursor.execute(selectQuery)
    postsArray = []
    for post in cursor:
        postsArray.append({
            "id": post[0],
            "company_id": post[1], 
            "content": post[2], 
            "likes_count": post[3], 
            "comments_count": post[4], 
            "retweets_count": post[5], 
            "created_time": post[6]
        })
    return postsArray

def getPostsByCompanyId(companyId, cursor):
    selectQuery = ("SELECT id, company_id, content, likes_count, comments_count, retweets_count, created_time FROM posts WHERE company_id=%s")
    cursor.execute(selectQuery, (companyId,))
    postsArray = []
    for result in cursor:
        postsArray.append({
            "id": result[0],
            "company_id": result[1], 
            "content": result[2], 
            "likes_count": result[3], 
            "comments_count": result[4], 
            "retweets_count": result[5], 
            "created_time": result[6]
        })
    return postsArray

def insertPost(companyId, message, likesCount, commentsCount, retweetsCount, createdTime, cursor):
    insertQuery = ("INSERT INTO posts (company_id, content, likes_count, comments_count, retweets_count, created_time) VALUES (%s, %s, %s, %s, %s)")
    postData = (companyId, message, likesCount, commentsCount, retweetsCount, createdTime)
    cursor.execute(insertQuery, postData)