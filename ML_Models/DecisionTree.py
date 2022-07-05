# Decision Tree ML Algorithm Method for Predicting Stock Movement
# decision tree method drawbacks : prone to over-fitting,
# and can be chaotic (sensitive to initial conditions)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import yfinance as yf

start = pd.datetime(2011, 1, 1)
end = pd.datetime(2021, 1, 1)

df = yf.download("AMZN", start, end)
df["Price_Up"] = np.where(df["Close"].shift(-1) > df["Close"], 1, 0)
#days where day after has higher close price are marked as 1

#Split data into independent data set X and dependent data set Y
X = df.iloc[:, 0:df.shape[1] -1].values  #gets all rows and cols apart from target
Y = df.iloc[:, df.shape[1]-1].values #Get all rows from target column

#Split the data into training (80%) and testing (20%)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
tree = DecisionTreeClassifier().fit(X_train, Y_train)


print(tree.score(X_train, Y_train)) #see model performance on training set
print(tree.score(X_test, Y_test)) #see model performance on testing set

#Show the model tree
tree_prediction = tree.predict(X_test)
print(tree_prediction)

print(Y_test)


# Conclusion here, the underlying model needs explaining as well as an overview
# of its outcome
# This method did not really work, for the stocks I used it only gets 0.5.
# Needs more training, testing and better data. Google was used in the original.


print("Debug")