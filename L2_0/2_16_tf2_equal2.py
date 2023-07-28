import tensorflow as tf

x1 = tf.constant([0.9,2.5,2.3,-4.5])
x2 = tf.constant([1.0,2.0,2.0,-4.0])
x3 = tf.Variable(x1)

print('x1: ',x1)
print('x2: ',x2)
print('r3: ',tf.round(x3))
print('eq: ',tf.equal(x1,x3))