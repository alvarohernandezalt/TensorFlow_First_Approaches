import tensorflow as tf 

x1 = tf.constant('café')
print("x1: ", x1)
tf.strings.length(x1)
print ("")

len1 = tf.strings.length(x1, unit="UTF8_CHAR")
len2 = tf.strings.unicode_decode(x1, "UTF8")

print("len1: ",len1.numpy())
print("len2: ",len2.numpy())
print("")

# string arrays
x2 = tf.constant(['Cafe', 'coffe', 'kaffe', 'taza'])
print('x2: ', x2)
print("")

len3 = tf.strings.length(x2, unit="UTF8_CHAR")
print('len3: ', len3.numpy())
print("")

r = tf.strings.unicode_decode(x2, "UTF8")
print("r: ", r)

