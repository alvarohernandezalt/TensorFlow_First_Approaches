''' 
How to use method chaining in order to invoke
the map() operator three times,
using three different lmbda expressions,
followed by the take()

'''
import tensorflow as tf 
import numpy as np 

x = np.array([[1],[2],[3],[4]])
print(x.shape)

# make a ds from a numpy array
ds = tf.data.Dataset.from_tensor_slices(x)
ds = ds.map(lambda x: ((x*2)+1)**3)

for value in ds:
    print('value: ',value)