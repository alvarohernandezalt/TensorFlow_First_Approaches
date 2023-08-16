"""
The reduce() operator performs a reduction on its input,
until a single value is produced.
For example, you can use the reduce() operator
to add all the numbers in a an array.

"""
import tensorflow as tf 
import numpy as np

x1 = tf.data.Dataset.range(8).reduce(np.int64(0), lambda x, _: x + 1)
x2 = tf.data.Dataset.range(8).reduce(np.int64(0), lambda x, y: x + y)

print('x1: ', x1)
print('x2: ', x2)