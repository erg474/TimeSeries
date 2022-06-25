import math
import sympy
import numpy as np
import matplotlib.pyplot as plt


plt.style.use("dark_background")

print(list(sympy.primerange(0,1000)))


def get_coordinate(num):
    return (num * np.cos(num), num*np.sin(num))


get_coordinate(1)

#matplotlib(x,y) = (get_coord

for x in sympy.primerange(0,1000):
    print(get_coordinate(x))

