import config
import database.db as db
import database.postDAO as postDAO
import database.companyDAO as companyDAO
import database.historicalStockPriceDAO as historicalStockPriceDAO
import quandl

quandl.ApiConfig.api_key = config.QUANDL

dbSelect = db.connect(config.DATABASE['user'], config.DATABASE['password'])
selectCursor = dbSelect.cursor()

dbInsert = db.connect(config.DATABASE['user'], config.DATABASE['password'])
insertCursor = dbInsert.cursor()

companies = companyDAO.getCompanies(selectCursor)

for company in companies:

    company_id = company['id']
    if company_id > 78:
        data = quandl.get('EOD/{}'.format(company['symbol']), start_date='2010-01-01', end_date='2019-07-28')

        for row in data.itertuples():        
            date = row[0].to_pydatetime()
            price = float(row[4])
            historicalStockPriceDAO.insertHistoricalStockPrice(company_id, price, date, insertCursor)

        dbInsert.commit()
        dbSelect.commit()

insertCursor.close()
selectCursor.close()
dbInsert.close()
dbSelect.close()