import config
import database.db as db
import database.postDAO as postDAO
import database.companyDAO as companyDAO


selectCursor = db.getCursor(config.DATABASE['user'], config.DATABASE['password'])

company = companyDAO.getCompany(400, selectCursor)

print(company)

companies = companyDAO.getCompanies(selectCursor)
for company in companies:
    print (company['name'])