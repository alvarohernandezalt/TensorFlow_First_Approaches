import tensorflow as tf 

x1 = tf.constant('café')
print("x1: ", x1)
tf.strings.length(x1)
print ("")

len1 = tf.strings.length(x1, unit="UTF8_CHAR")
len2 = tf.strings.unicode_decode(x1, "UTF8")

print("len1: ",len1.numpy())
print("len1: ",len2.numpy())
print("")

