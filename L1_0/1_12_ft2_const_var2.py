import tensorflow as tf

v1 = tf.Variable([4.0, 4.0])
c1 = tf.constant([1.0, 2.0])

diff = tf.substract(v1, c1)
print('Diff: ', diff.numpy())
