def getPost(id, cursor):
    selectQuery = ("SELECT id, company_id, source, content, likes_count, retweets_count, created_time FROM posts WHERE id=%s")
    cursor.execute(selectQuery, (id,))
    post = cursor.fetchone()
    return {
            "id": post[0],
            "company_id": post[1],
            "source": post[2], 
            "content": post[3], 
            "likes_count": post[4], 
            "retweets_count": post[5], 
            "created_time": post[6]
    }

def getPosts(cursor):
    selectQuery = ("SELECT id, company_id, content, source, likes_count, retweets_count, created_time FROM posts")
    cursor.execute(selectQuery)
    postsArray = []
    for post in cursor:
        postsArray.append({
            "id": post[0],
            "company_id": post[1],
            "source": post[2], 
            "content": post[3], 
            "likes_count": post[4], 
            "retweets_count": post[5], 
            "created_time": post[6]
        })
    return postsArray

def getPostsByCompanyId(companyId, cursor):
    selectQuery = ("SELECT id, company_id, source, content, likes_count, retweets_count, created_time FROM posts WHERE company_id=%s")
    cursor.execute(selectQuery, (companyId,))
    postsArray = []
    for post in cursor:
        postsArray.append({
            "id": post[0],
            "company_id": post[1],
            "source": post[2], 
            "content": post[3], 
            "likes_count": post[4], 
            "retweets_count": post[5], 
            "created_time": post[6]
        })
    return postsArray

def insertPost(companyId, source, message, likesCount, retweetsCount, createdTime, cursor):
    insertQuery = ("INSERT INTO posts (company_id, source, content, likes_count, retweets_count, created_time) VALUES (%s, %s, %s, %s, %s)")
    postData = (companyId, source, message, likesCount, retweetsCount, createdTime)
    cursor.execute(insertQuery, postData)

def insertPostVisualization(postId, html, cursor):
    insertQuery = ("INSERT INTO post_visualization_html (post_id, html) VALUES (%s, %s)")
    postVisualizationData = (postId, html)
    cursor.execute(insertQuery, postVisualizationData)
