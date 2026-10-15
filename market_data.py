import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ticker = yf.Ticker('SPY')
# prices = ticker.history(period='10y')
# print(prices.head())
# print(prices.tail())
# print(prices.shape)
# prices.to_csv('data/spy.csv')

prices = pd.read_csv('data/spy.csv', index_col=0)
prices.index = pd.to_datetime(prices.index, utc=True)

close = prices['Close']

r_t = np.log(close/close.shift(1)).dropna()
print(r_t.head())
daily_vol = r_t.std()
annual_vol = daily_vol*np.sqrt(252)
print('daily volatility: ', daily_vol)
print(f'annual volatility: {annual_vol:.1%}')

plt.plot(r_t.index, r_t)
plt.xlabel('Date')
plt.ylabel('Daily log return')
plt.title('SPY Daily Log Returns, 2016-2026')
plt.show()