"""
The filter() operator uses Boolean logic to "filter" the elements in an array,
in order to determine which elements satisfy the Boolean condition.

"""

import tensorflow as tf 
import numpy as np

#def filter_fn(x):
#   return tf.reshape(tf.not_equal(x % 2, 1), [])

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.filter(lambda x: tf.reshape(tf.not_equal(x%3, 0), []))

#ds = ds.filter(fiter_function)

for value in ds: 
    print('value: ',value)