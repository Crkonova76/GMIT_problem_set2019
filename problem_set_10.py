# Martina Crkonova, 2019-03-24
# Problem Set 2019, Python plot, Programming and Scripting, GMIT
# Program which displays a plot of functions

# Import libary section 
import matplotlib.pyplot as plt
import numpy as np

# x is assigned to numpy array of the range zero to four
x = np.array(range(0, 4))
# b is output of calculation x multiplied by x
b = x * x
# c is two power by x
c = 2**x

# Specify the arguments of the plot
plt.plot(x, x, label='linear function', linewidth=2)
plt.plot(x, b, label='square function', linewidth=2)
plt.plot(x, c, label='exponential function',linewidth=2)

# Display legend of the plot as specify in above lines
plt.legend()

# Specifications of the grid
plt.grid(True, color='0.7', linestyle = '--')

# Display the plot
plt.show()