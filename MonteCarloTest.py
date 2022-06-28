import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# Initialising Stock Data
start = dt.datetime(2011,1,1)
end = dt.datetime(2021,1,1)

stock_data = yf.download('MSFT', start, end) #Microsoft
stock_data_close = stock_data['Close']

plt.plot(stock_data_close)
plt.title("MSFT (Microsoft) Stock between 2011 and 2021")
plt.ylabel("Price")

plt.show()


returns = stock_data['Adj Close'].pct_change()
daily_vol = returns.std()
rate_of_return = (stock_data['Open'] - stock_data['Close']) / stock_data['Open']

# Single Random Walk for Future Trading Year
T = 252 #252 trading days
count = 0
price_list = []
last_price = stock_data['Adj Close'][-1]

price = last_price * (1 + np.random.normal(0, daily_vol))
price_list.append(price)

# Generate a random walk, step is a normal curve where sd = daily vol
for y in range(T):
    #if count == 251:
    #    break
    price = price_list[count] * (1 + np.random.normal(0, daily_vol))
    price_list.append(price)
    count += 1

plt.plot(price_list)
plt.title("Random Walk From Last MSFT Price")
plt.ylabel("Price")
plt.xlabel("Trading Days over a year")
plt.show()