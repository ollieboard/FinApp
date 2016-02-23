# class for stock depot - simulator
import stock
import ystockquote

class Depot(object):
    
    def __init__(self, total, stocks, maxStocks):
        self.total = total # available money in depot
        self.stocks = stocks # stocks already in depot
        self.maxStocks = maxStocks # max stocks to be held at one time

    # method for getting stock price via ystockquote:
    # def getStockPrice(self, name):
    #    allInfo = ystockquote.get_all(name)
    #    return float(allInfo["price"])

    # method for getting historical stock price:
    # def getStockHistory(self, name, start, end):
    #    allInfo = ystockquote.get_historical_prices(name, start, end)
    #    return allInfo

    # method for buying stock
    def buyStock(self, stock):
        pass

    # method for selling stock
    def sellStock(self, stock):
        pass

    # method for calculating worth of depot:
    def depotWorth(self):
	tot = 0
	for i in self.stocks:
	    price = i.getStockPrice()
	    tot += price * i.amount
	return tot
    

money = 1000 # available money in depot
stockTSLA = stock.Stock('TSLA', 150, 10)
stockAIRB = stock.Stock('AIR.DE', 50, 2)
stocks = [stockTSLA, stockAIRB] # available stocks
trialDepot = Depot(money, stocks, 5)

for i in stocks:
    print i

print trialDepot.depotWorth()

print stocks[0].getStockHistory('2015-12-12', '2016-02-20')
