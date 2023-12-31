import tensorflow as tf 

x = tf.constant([[1.,2.,3.],[4.,5.,6.]])

print("x: ", x)
print("")
print("x.shape: ", x.shape)
print("")
print("x.dtype: ", x.dtype)
print("")
print("x[:,1:]: ", x[:,1:])
print("")
print("x[...,1,tf.newaxis]: ", x[...,1,tf.newaxis])
print("")
print("x + 10: ", x + 10)
print("")
print("tf.square(x): ", tf.square(x))
print("")
print("x @ tf.transpose(x): ", x @ tf.transpose(x))

m1 = tf.constant([[1.,2.,4.],[3.,6.,12.]])
print("m1:            ", m1)
print("m1 + 50:       ", m1 + 50)
print("m1 * 2:        ", m1 * 2)
print("tf.square(m1): ", tf.square(m1))

