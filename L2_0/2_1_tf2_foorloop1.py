# using for loops in tensorflow

import tensorflow as tf

x = tf.Variable(0, name='x')

for i in range(5):
    x = x + 1
    print('x: ',x.numpy())