import tensorflow as tf

x = tf.constant([100,200,300], name = 'x')
y = tf.constant([1,2,3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
