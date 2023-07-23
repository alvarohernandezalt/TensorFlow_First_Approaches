import tensorflow as tf

v1 = tf.Variable([4.0, 4.0])
c1 = tf.constant([1.0, 2.0])

diff = tf.subtract(v1, c1)
print("Diff1: ", diff.numpy())

# diff is NOT updated
v1.assign([10.0, 20.0])
print("Diff2: ", diff.numpy())

# diff updated
diff = tf.subtract(v1, c1)
print("Diff3: ", diff.numpy())
