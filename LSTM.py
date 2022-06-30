# LSTM - Long Short Term Memory
# ML Stock Models don't often work is due to poor implementation/understanding
# LSTMs are one of the most widely used and successful ML financial algorithm
# when paired with the correct problems are datasets

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import yfinance as yf

from tensorflow import keras
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#the above 2 lines sync matplotlib and pandas plotting functions

def create_dataset(X, y, time_steps=1): #capital X
    Xs, ys = [], []
    for i in range(len(X) - time_steps):
        v = X.iloc[i:(i + time_steps)].values
        Xs.append(v)
        ys.append(y.iloc[i + time_steps])
    return np.array(Xs), np.array(ys)

ticker = yf.Ticker("MSFT")
data = ticker.history(period = "15y", interval = "1d")
data.sort_values('Date', inplace=True, ascending=True)
print(data.head())

plt.figure(num=None, figsize=(15,6), dpi=80, facecolor='w', edgecolor='k')
data['Close'].plot()
plt.tight_layout()
plt.grid()
#plt.show()

df = data[['Close']].copy()
#split data into train and test
train, test = df.iloc[0:-200], df.iloc[-200:len(df)]
print(len(train), len(test))

train_max = train.max()
train_min = train.min()

#Normalize the dataframes
train = (train - train_min) / (train_max - train_min)
test  = (test - train_min) / (train_max - train_min)
#NOTE: When normalizing data, do not normalize the test data separately


time_steps = 10

X_train, y_train = create_dataset(train, train.Close, time_steps)
X_test, y_test = create_dataset(test, test.Close, time_steps)

model = keras.Sequential()
model.add(keras.layers.LSTM(250, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1))
model.compile(loss='mae', optimizer='adam')
model.summary()

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32
    shuffle=False
)
