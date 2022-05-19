#Stock Market Simulator that uses Yahoo Finance Time Series Data
import yfinance as yf
import matplotlib.pyplot as  plt
import seabornm


msft = yf.Ticker("MSFT")
print(msft.info)

hist = msft.history(period="5d")
