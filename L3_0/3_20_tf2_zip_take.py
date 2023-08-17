import tensorflow as tf 
import numpy as np 

x = np.arange(0,10)
y = np.arange(1,11)

# create dataset objects from the arrays
dx = tf.data.Dataset.from_tensor_slices(x) 
dy = tf.data.Dataset.from_tensor_slices(y)

zip the two datasets together