import tensorflow as tf
import numpy as np

elems = np.array([1, 2, 3, 4, 5])

doubles = tf.map_fn(lambda x : 2 * x, elems)
print('doubles: ', doubles)

squares = tf.map_fn(lambda x : x * x, elems)
print('squares: ', squares)

