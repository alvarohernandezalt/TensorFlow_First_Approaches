''' 
flat_map() takes a function that maps a single element of the input 
dataset to a Dataset of elements

'''

import tensorflow as tf 
import numpy as np 


x = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

ds = tf.data.Dataset.from_tensor_slices(x)
ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(x))

for value in ds:
    print('value:',value)