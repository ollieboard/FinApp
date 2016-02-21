# Method for stock depot - simulator
import ystockquote

# method for getting stock price via ystockquote:
def getStockPrice(stock):
    allInfo = ystockquote.get_all(stock)
    return allInfo["price"]

# method for getting historical stock price:

def getStockHistory(stock, start, end):
    allInfo = ystockquote.get_historical_prices(stock, start, end)
    return allInfo


total = 1000 # available money in depot

stocks = ['TSLA']


price = getStockHistory(stocks[0], '2010-01-01', '2016-02-01')

print price


