# See Momentum (strengths and weaknesses) of stocks. Three Components:
    # 1. Move Moving Average of different lengths to detect long-term trend
    # 2. Use 52-week low and high as lower bound and upper breakthrough
    # 3. RSI (relative strength) greater than 80, not to see overbought stocks,
    # but to screen stocks with an extended upward trend - here RSI>80 for a long time

# Rules for this Momentum Screener
    # 1. Current price above 150 & 200 days moving average (MA)
    # 2. 150 days A > 200 days MA
    # 3. 200 days MA trending up for at least 1 month
    # 4. 50 MA > 150 and 200 MAs
    # 5. Stock price is above the 50 day MA
    # 6. Current share price is at least 30% above 52 week low
    # 7. Current stock price is at least within 25% of the 52 week high
    # 8. RSI is about 80 (isn't 80 bad overbought...?)


# this system seems quite inclined to the tenets of Technical Analysis

# actually just use this link locally
# https://medium.com/@chris_42047/building-a-super-momentum-stock-screener-for-thousands-of-stocks-python-446c0298f7e8