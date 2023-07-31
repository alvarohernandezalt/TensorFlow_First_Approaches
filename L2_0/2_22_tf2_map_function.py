import tensorflow as tf
import numpy as np

elems = np.array([1, 2, 3, 4, 5])

doubles = tf.map_fn(lambda x : 2 * x, elems)
print('doubles: ', doubles)

squares = tf.map_fn(lambda x : x * x, elems)
print('squares: ', squares)

elems = (np.array([1,2,3]), np.array([-1,1,-1]))
neg_pos = tf.map_fn(lambda x: x[0] * x[1], elems, dtype=tf.int64)
print('neg_pos: ', neg_pos)

elems = np.array([1,2,3])
pos_neg = tf.map_fn(lambda x: (x, -x), elems, dtype =(tf.int64, tf.int64))
print('pos_neg: ', pos_neg)
