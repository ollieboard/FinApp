# Method for stock depot - simulator
import ystockquote

class Depot(object):

    def __init__(self, total, stocks):
        self.total = total
        self.stocks = stocks

    # method for getting stock price via ystockquote:
    def getStockPrice(self):
        allInfo = ystockquote.get_all(self.stocks)
        return allInfo["price"]

    # method for getting historical stock price:
    def getStockHistory(self, start, end):
        allInfo = ystockquote.get_historical_prices(self.stocks, start, end)
        return allInfo


money = 1000 # available money in depot
stocks = ['TSLA'] # available stocks
trialDepot = Depot(money, stocks)

print trialDepot.getStockPrice()
