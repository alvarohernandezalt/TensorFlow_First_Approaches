"""
ds = tf.data.Dataset.from_generator(gener, (tf.int64))

The dataset ds obtains its values from the Python function gener(),
that emits a value of type tf.int64

"""

import tensorflow as tf 
import numpy as np 

x= arange(0,10)
def gener():
    for i in x:
        yield (3*i)

ds = tf.data.Datset.from_generator(gener, (tf.int64))

for value in ds.take(len(x)):
    print('value: ',value)