import tensorflow as tf 
import numpy as np

# Simple numpy array
x = np.array([[1],[2],[3],[4]])

# Make a dataset from a NumPy array
datset = tf.data.Dataset.from_tensor_slices(x)
