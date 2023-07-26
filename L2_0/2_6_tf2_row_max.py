import tensorflow as tf

# initialize an array of arrays
a = [[1,2,3],[30,20,10],[40,60,50]]
b = tf.Variable(a, name='b')

print('b: ', tf.argmax(b,1))

# tf.argmax determines the inddex values containing the maximun
# values on a row-wise basis or on a column-wise basis

