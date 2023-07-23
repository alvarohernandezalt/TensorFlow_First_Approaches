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