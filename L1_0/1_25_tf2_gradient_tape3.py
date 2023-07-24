# Using nested Loops with tf.GradientTape

import tensorflow as tf 

x = tf.constant(4.0)
with tf.GradientTape() as t1:
    with tf.GradientTape() as t2:
        t1.watch(x)
        t2.watch(x)
        z = x * x * x
    dz_dx = t2.gradient(z, x)
dz2_dx2 = t1.gradient(dz_dx, x)

print('First dz_dx: ', dz_dx)
print('Second dz2_dx2: ', dz2_dx2)


