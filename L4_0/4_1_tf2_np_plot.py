import numpy as np
import matplotlib.pyplot as plt

# Create a pseudo-random x,y values for plotting purposes.

# Return smaples with shape(15,1) with standard normal distribution
x = np.random.randn(15, 1)
# Add pseudo randomness to y paired values 
y = 2.5*x + 5 + 0.2*np.random.randn(15,1)

print('x: ',x)
print('y: ',y)

plt.scatter(x,y)
plt.show()