#do a monte carlo test based off of financial data

import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

start = dt.datetime(2011,1,1)
end = dt.datetime(2021,1,1)

stock_data = yf.download('MSFT', start, end) #Microsoft

returns = stock_data['Adj Close'].pct_change()
daily_vol = returns.std()
rate_of_return = (stock_data['Open'] - stock_data['Close']) / stock_data['Open']
print(rate_of_return)

