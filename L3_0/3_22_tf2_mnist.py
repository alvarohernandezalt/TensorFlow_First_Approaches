''' 
How to create a dataset from an existing one:
In this case MNIST dataset

'''

import tensorflow as tf 

train, test = tf.keras.datasets.mnist.load_data()
mnist_x, mnist_y = train

print('mnist_x.shape: ',mnist_x.shape)
print('mnist_y.shape: ',mnist_y.shape)

mnist_ds = tf.data.Dataset.from_tensor_slices(mnist_x)
#print(mnist_ds)

for value in mnist_ds.take(100):
    print('value: ', value)

