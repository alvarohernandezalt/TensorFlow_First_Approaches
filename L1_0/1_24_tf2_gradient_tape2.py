import tensorflow as tf

x = tf.constant(3.0)

with tf.GradientTape() as g:
    g.watch(x)
    y = 4 * x * x

dx_dy = g.gradient(y,x)
print(dx_dy)
