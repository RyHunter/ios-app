import config
import database.db as db
import database.postDAO as postDAO
import database.companyDAO as companyDAO
import database.tokenDAO as tokenDAO
import spacy
from spacy import displacy

dbSelect = db.connect(config.DATABASE['user'], config.DATABASE['password'])
selectCursor = dbSelect.cursor()

dbInsert = db.connect(config.DATABASE['user'], config.DATABASE['password'])
insertCursor = dbInsert.cursor()

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
        html = displacy.render(doc, style="dep")
        postDAO.insertPostVisualization(post['id'], html, insertCursor)
        for token in doc:
            tokenDAO.insertToken(post['id'], token.text, token.lemma_, token.pos_, insertCursor)


dbInsert.commit()
dbSelect.commit()
insertCursor.close()
selectCursor.close()
dbInsert.close()
dbSelect.close()