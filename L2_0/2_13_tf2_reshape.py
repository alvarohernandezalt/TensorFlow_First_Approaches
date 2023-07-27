import tensorflow as tf

x = tf.constant([[2,5,3,-5],[0,3,-2,5],[4,3,5,3]])

print("shape: ", tf.shape(input=x))
print("shape: ", tf.reshape(x, [6,2]))
print("shape: ", tf.reshape(x, [3,4]))
