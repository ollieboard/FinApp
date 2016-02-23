# test function for depot and stocks
import depot
import stock
import stockMath
import matplotlib.pyplot as plt

money = 1000
stockTSLA = stock.Stock('TSLA', 150, 10)
stockAIRB = stock.Stock('AIR.DE', 50, 2)
stocks = [stockTSLA, stockAIRB]
trialDepot = depot.Depot(money, stocks, 5)

for i in stocks:
    print i

print trialDepot.depotWorth()

history = stocks[0].getStockHistory('2015-12-12', '2016-02-20')

print type(history)
historyList = []
#for i in history:
#    historyList.append(i['close'])

#plt.plot(historyList)
#plt.ylabel('stock prices ($)')
#plt.show()
