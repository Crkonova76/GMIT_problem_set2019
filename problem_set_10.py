# Martina Crkonova, 2019-03-18
# Problem Set 2019, Python second, Programming and Scripting, GMIT
# Program which displays a plot of functions

import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(0, 4))
b = x * x
c = 2**x

plt.plot(x, x,label='linear function', linewidth=2)
plt.plot(x, b, label='square function', linewidth=2)
plt.plot(x, c, label='exponential function',linewidth=2)

plt.legend()

plt.grid(True, color='0.7', linestyle = '--')

plt.show()