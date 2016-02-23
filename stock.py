# class for stocks

class Stock(object):

    def __init__(self, name, buyPrice, amount):
        self.name = name
        self.buyPrice = buyPrice
        self.amount = amount

    def __str__(self):
		return "Name: %s, Price bought: %s, Amount: %s" % (self.name, self.buyPrice, self.amount)

    
