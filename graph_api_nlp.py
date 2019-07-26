import config
import database.db as db
import database.postDAO as postDAO
import database.companyDAO as companyDAO
import spacy

db = db.connect(config.DATABASE['user'], config.DATABASE['password'])
selectCursor = db.cursor()

nlp = spacy.load("en_core_web_sm")

# for testing only
id = 430
testCompany = companyDAO.getCompany(id, selectCursor)
companiesArray = [testCompany]

# companiesArray = companyDAO.getCompanies(selectCursor)
for company in companiesArray:
    posts = postDAO.getPostsByCompanyId(company['id'], selectCursor)
    for post in posts:
        doc = nlp(post['content'])
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)