#Test Financial Methods (TA, Fundemental, Quant) on a Random Walk as a sort of Control Group
import numpy as np
import matplotlib.pyplot as plt

steps = np.random.normal(loc=0, scale=5, size=100000)
#print(steps)

steps[0]=0

P = 100 + np.cumsum(steps)

plt.plot(P)
plt.title("Simulated Random Walk")
plt.show()
print("done")