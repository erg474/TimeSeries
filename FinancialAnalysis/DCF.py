#Intrinsic stock evaluation, Discounted Cash Flow Models
#DCF Models are a way to calculate the intrinsic value of a company
#This can tell you whether or not a Company is overvalued
#https://medium.com/swlh/intrinsic-valuation-of-stocks-using-python-5d902a34b1a0

import numpy as np
import pandas as pd

years=['2019A', '2020F', '2021F', '2022F', '2023F', '2024F']
sales = pd.Series(index=years)
sales['2019A'] = 15
print(sales)

nwc_percent = 0.24
nwc = sales * nwc_percent
change