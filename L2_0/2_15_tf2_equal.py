import tensorflow as tf

x1 = tf.constant([0.9,2.5,2.3,-4.5])
x2 = tf.constant([1.0,2.0,2.0,-4.0])
eq = tf.equal(x1,x2)
neq = tf.not_equal(x1,x2)

