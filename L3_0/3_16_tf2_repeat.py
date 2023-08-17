# repeat() just repeats its input 'n' times

import tensorflow as tf 

ds = tf.data.Dataset.from_tensor_slices(tf.range(4))
ds = ds.repeat(2)

for values in ds:
    print(values)

    