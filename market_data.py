import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs('images', exist_ok=True)
from scipy.stats import norm


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
average_annual_return = r_t.mean() * 252
print('daily volatility: ', daily_vol)
print(f'annual volatility: {annual_vol:.1%}')
print(f'average annual return: {average_annual_return:.1%}')

mu = r_t.mean()
sigma = daily_vol
x = np.linspace(r_t.min(), r_t.max(), 500)
normal_pdf = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x - mu)**2/(2*sigma**2))
extreme_days = ((r_t - mu).abs() > 4 * daily_vol).sum()
p = 2*norm.cdf(-4)
expected_days = p * len(r_t)
print('P(|r - mu| > 4 * sigma) =', p)
print('expected (normal):', expected_days)
print('actual (SPY):', extreme_days)
print('excess kurtosis:', r_t.kurt())
r_no_2020 = r_t[r_t.index.year != 2020]
print('excess kurtosis without 2020: ', r_no_2020.kurt())
rolling_vol = r_t.rolling(21).std() * np.sqrt(252)
print(f'highest rolling volatility: {rolling_vol.max():.1%} on {rolling_vol.idxmax().date()}')
print(f'lowest rolling volatility: {rolling_vol.min():.1%} on {rolling_vol.idxmin().date()}')
print(f"today's value: {rolling_vol.iloc[-1]:.1%}")

plt.plot(r_t.index, r_t)
plt.xlabel('Date')
plt.ylabel('Daily log return')
plt.title('SPY Daily Log Returns, 2016-2026')
plt.savefig('images/daily_returns.png', dpi=150, bbox_inches='tight')
plt.figure()
plt.hist(r_t, bins=100, density=True, label='SPY returns')
plt.title('Distribution of SPY Daily Log Returns')
plt.xlabel('Daily log return')
plt.ylabel('Density')
plt.plot(x, normal_pdf, color='red', label='Normal distribution')
plt.legend(loc = 'upper left')
plt.savefig('images/return_distribution.png', dpi=150, bbox_inches='tight')
plt.figure()
plt.plot(rolling_vol.index, rolling_vol, label='21-day rolling volatility')
plt.axhline(annual_vol, color='red', linestyle='--', label='10-year average')
plt.title('SPY 21-Day Rolling Volatility (Annualised), 2016-2026')
plt.xlabel('Date')
plt.ylabel('Annualised volatility')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.PercentFormatter(1.0))
plt.legend(loc = 'upper left')
plt.savefig('images/rolling_volatility.png', dpi=150, bbox_inches='tight')
plt.show()