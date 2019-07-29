def getCompany(id, cursor):
    selectQuery = ("SELECT id, url, name, twitter_handle, twitter_handle_is_facebook_url, symbol FROM companies WHERE id=%s")
    cursor.execute(selectQuery, (id,))
    company = cursor.fetchone()
    return {
            "id": company[0], 
            "url": company[1], 
            "name": company[2], 
            "twitter_handle": company[3], 
            "twitter_handle_is_facebook_url": company[4],
            "symbol": company[5],
    }

def getCompanies(cursor):
    selectQuery = ("SELECT id, url, name, twitter_handle, twitter_handle_is_facebook_url, symbol FROM companies")
    cursor.execute(selectQuery)
    companiesArray = []
    for company in cursor:
        companiesArray.append({
            "id": company[0], 
            "url": company[1], 
            "name": company[2], 
            "twitter_handle": company[3], 
            "twitter_handle_is_facebook_url": company[4],
            "symbol": company[5],
        })
    return companiesArray