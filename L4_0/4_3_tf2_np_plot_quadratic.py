import numpy as np
import matplotlib.pyplot as plt


# See what happens with this set of values:
# x = np.linspace(-5,5,num=100) 
# [:,None] this convert a vector into a 2D array
x = np.linspace(-5,5,num=100) [:,None]
y = -0.5 + 2.2*x +0.3*x**2 + 2*np.random.randn(100,1)

plt.scatter(x,y)
plt.show()