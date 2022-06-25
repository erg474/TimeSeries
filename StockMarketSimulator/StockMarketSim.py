#Stock Market Simulator that uses Yahoo Finance Time Series Data
import yfinance as yf
import matplotlib.pyplot as  plt
import seaborn

#For this task, the module yfinance is useful and has many uses

msft = yf.Ticker("MSFT")
print(msft.info)

hist = msft.history(period="5d")
hist['Close'].plot(figsize=(16,9))
plt.show()