def insertHistoricalStockPrice(companyId, price, date, cursor):
    print(companyId, price, date)
    insertQuery = ("INSERT INTO historical_stock_prices (company_id, price, date) VALUES (%s, %s, %s)")
    priceData = (companyId, price, date)
    cursor.execute(insertQuery, priceData)