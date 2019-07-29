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
    data = quandl.get_table('WIKI/PRICES', 
                            qopts = { 'columns': ['ticker', 'date', 'close'] }, 
                            ticker = [company['symbol']], 
                            date = { 'gte': '2010-01-01', 'lte': '2019-7-27' })
    company_id = company['id']
    numRows = data.index.stop
    for i in range(numRows):
        date = data.at[i, 'date'].to_pydatetime()
        price = float(data.at[i, 'close'])
        historicalStockPriceDAO.insertHistoricalStockPrice(company_id, price, date, insertCursor)

dbInsert.commit()
dbSelect.commit()
insertCursor.close()
selectCursor.close()
dbInsert.close()
dbSelect.close()