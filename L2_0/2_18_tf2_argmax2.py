import tensorflow as tf

# initialize array of arrays
arr1 = [[1,2,3],[30,20,10],[40,50,60]]
b = tf.Variable(arr1, name='b')

print("index of max values in b: ", tf.argmax(input=b, axis=1))
