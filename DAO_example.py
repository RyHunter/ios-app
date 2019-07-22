import config
import database.db as db
import database.postDAO as postDAO
import database.companyDAO as companyDAO

# Make a connection and grab a cursor
db = db.connect(config.DATABASE['user'], config.DATABASE['password'])
selectCursor = db.cursor()

# Get one company by its id
company = companyDAO.getCompany(400, selectCursor)
print(company['twitter_handle'])

# Get all companies in an array of dicts
companies = companyDAO.getCompanies(selectCursor)
for c in companies:
    print(c['name'])

# Get one post by id
post = postDAO.getPost(400, selectCursor)
print(post['content'])

# Get all posts in an array of dicts
posts = postDAO.getPosts(selectCursor)
for post in posts:
    print(post['likes_count'])

# Get all posts by one company using company 400
posts = postDAO.getPostsByCompanyId(430, selectCursor)
for post in posts:
    print(post['created_time'])