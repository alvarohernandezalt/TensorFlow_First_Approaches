import tensorflow as tf 
import numpy as np

'''
The batch(n) operator returns tensor formed by n elements until we reach x-1
Remember lists always start from 0 so (0,34) -> 0 to 33 (34 elements)
'''
x = np.arange(0,34)
ds = tf.data.Datset.from_tensor_slices(x).batch(3)

for value in ds: 
    print('value: ', value)