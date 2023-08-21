import numpy as np
import matplotlib.pyplot as plt

# x Returns 11 evenly spaced samples, calculated over the interval [-1, 1].
x_data = np.linspace(-1, 1, 11)
# Create some perturbance in the y pairs for real regression model
y_data = 4*x_data + np.random.randn(*x_data.shape)*0.5

plt.scatter(x_data, y_data)
plt.show()