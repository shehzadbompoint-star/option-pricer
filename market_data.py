import yfinance as yf
import matplotlib.pyplot as plt

ticker = yf.Ticker('SPY')
prices = ticker.history(period='10y')
print(prices.head())
print(prices.tail())
print(prices.shape)
prices.to_csv('data/spy.csv')

plt.plot(prices.index, prices['Close'])
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('SPY Daily Closing Price (Adjusted), 2016-2026')
plt.show()