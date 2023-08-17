import tensorflow as tf 
import numpy as np

x = np.arange(0, 12)

def gener():
    i=0
    while(i < len(x/3)):
        yield (i, i+1, i+2)
        i += 3

ds = tf.data.Dataset.from_generator(gener, (tf.int64, tf.int64, tf.int64))

third = int(len(x)/3)
for value in ds.take(third):
    print('value: ', value)

### NOTE: look also 3__5_tf2_generator.py and compare and experiment...