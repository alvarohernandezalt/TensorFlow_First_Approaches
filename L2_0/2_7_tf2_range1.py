import tensorflow as tf


# tf.range takes an initial number and a final one. 
# Generate an array of the values that goes from init to end counted by the third number/variable

a1 = tf.range(3,18,3)
b2 = tf.range(1,133,11)

print('a1: ', a1)
print('b2: ', b2)