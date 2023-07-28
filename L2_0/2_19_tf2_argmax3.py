import tensorflow as tf
import numpy as np

x = np.array([[31, 23,  4, 54],
              [10,  3, 25,  0],
              [28, 14, 33, 22],
              [17, 12,  5, 81]])

y = np.array([[31, 23,  4, 24],
              [18,  3, 25,  0],
              [28, 14, 33, 22],
              [17, 12,  5, 11]])

print('xmax: ',tf.argmax(input=x,axis=1))
print('ymax: ',tf.argmax(input=y,axis=1))
print('equal: ',tf.equal(x,y))