import tensorflow as tf
import numpy as np

x1 = tf.constant([3.9, 2.1, 2.3, -4.0])
x2 = tf.constant([1.0, 2.0, 5.0, -4.2])

print('x1: ',x1)
print('x2: ',x2)
print('a1: ',tf.argmax(input=x1, axis=0))
print('a2: ',tf.argmax(input=x2, axis=0))