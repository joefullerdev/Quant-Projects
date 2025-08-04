import yfinance as yf
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

class SMACross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

msft = yf.Ticker("MSFT")
msftHist = msft.history(period="10y")
msftHist.index = pd.to_datetime(msftHist.index)
msftHist = msftHist[['Open', 'High', 'Low', 'Close', 'Volume']]

bt = Backtest(msftHist, SMACross, cash=10000, commission=0.002, exclusive_orders=True)

output = bt.run()
print(output)
bt.plot()
