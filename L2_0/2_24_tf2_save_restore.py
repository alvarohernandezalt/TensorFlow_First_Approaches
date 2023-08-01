import tensorflow as tf

x = tf.Variable(10.)
# Checkpoint = tf.train.Checkpoint()
checkpoint = tf.train.Checkpoint(x=x)
print('x: ',x)