import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import finplot as fplt
import pytz  # time zone management
import MetaTrader5  # importing OHLC data

# Initialising Stock Data
start = dt.datetime(2011, 1, 1)
end = dt.datetime(2021, 1, 1)

stock_data = yf.download('MSFT', start, end)  # Microsoft
stock_data_close = stock_data['Close']

plt.plot(stock_data_close)
plt.title("MSFT (Microsoft) Stock between 2011 and 2021")
plt.ylabel("Price")
# plt.show()

df_msft = yf.download('MSFT', '2011-01-01', '2021-01-01')
fplt.candlestick_ochl(df_msft[['Open', 'Close', 'High', 'Low']])
# fplt.show()
print("\n")

returns = stock_data['Adj Close'].pct_change()
daily_vol = returns.std()
rate_of_return = (stock_data['Open'] - stock_data['Close']) / stock_data['Open']

# Single Random Walk for Future Trading Year
T = 252  # 252 trading days
count = 0
price_list = []
last_price = stock_data['Adj Close'][-1]

price = last_price * (1 + np.random.normal(0, daily_vol))
price_list.append(price)

# Generate a random walk, step is a normal curve where sd = daily vol
for y in range(T):
    # if count == 251:
    #    break
    price = price_list[count] * (1 + np.random.normal(0, daily_vol))
    price_list.append(price)
    count += 1

plt.plot(price_list)
plt.title("Random Walk From Last MSFT Price")
plt.ylabel("Price")
plt.xlabel("Trading Days over a year")
# plt.show()

# Monte Carlo Simulation
num_simulations = 1000
df = pd.DataFrame()
last_price_list = []
for x in range(num_simulations):
    count = 0
    price_list = []
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_list.append(price)  # initial price

    for y in range(T):
        price = price_list[count] * (1 + np.random.normal(0, daily_vol))
        price_list.append(price)
        count += 1

    df[x] = price_list  # creates a df column (or row?) for each Random Walk
    last_price_list.append(price_list[-1])

fig = plt.figure()
fig.suptitle("Monte Carlo Simulation: MSFT")
plt.plot(df)
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()

# Mean and Percentiles
print("Expected price: ", np.mean(last_price_list))  # to round add round(etc, 2)
print("Quantile (5%):  ", np.percentile(last_price_list, 5))
print("Quantile (95%): ", np.percentile(last_price_list, 95))

# Histogram
plt.hist(last_price_list, bins=100)
plt.axvline(np.percentile(last_price_list, 5), color='r', linestyle='dashed', linewidth=2)
plt.axvline(np.percentile(last_price_list, 95), color='r', linestyle='dashed', linewidth=2)
plt.show()
