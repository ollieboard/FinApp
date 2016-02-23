# class for stocks
import ystockquote

class Stock(object):

    def __init__(self, name, buyPrice, amount):
        self.name = name
        self.buyPrice = buyPrice
        self.amount = amount

    def __str__(self):
		return "Name: %s, Price bought: %s, Amount: %s" % (self.name, self.buyPrice, self.amount)

    # get current stock price        
    def getStockPrice(self):
        allInfo = ystockquote.get_all(self.name)
        return float(allInfo["price"])

    # get historical stock prices. Date format for start end: "YYYY-MM-DD"
    def getStockHistory(self, start, end):
        allInfo = ystockquote.get_historical_prices(self.name, start, end)
        return allInfo
