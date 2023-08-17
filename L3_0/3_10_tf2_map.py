'''
The map() operator "applies" a lambda expression
to each input element

'''

import tensorflow as tf 
import numpy as np

x = np.array([[1],[2],[3],[4]])
ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.map(lambda x: (x*2)*3)

for value in ds:
    print(value)