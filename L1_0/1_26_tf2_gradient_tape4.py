# how to use tf.gradientTape in order to calculate first derivative ->
# of an expression that depends on a 2x2 tensor in TF 2

import tensorflow as tf 

x = tf.ones((3,3))

with tf.GradientTape() as t:
    t.watch(x)
    y = tf.reduce_sum(x)
    print('y: ',y)
    z = tf.multiply(y,y)
    print('z: ',z)
    z = tf.multiply(z,y)
    print('z: ',z)

# the derivative of z with respect to y
dz_dy = t.gradient(z, y)
print('dz_dy: ',dz_dy)