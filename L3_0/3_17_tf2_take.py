# Taking n input values from the dataset

import tensorflow as tf 

ds = tf.data.Dataset.from_tensor_slices(tf.range(8))
ds = ds.take(5)

# As we have noe reduced the dataset to 5 elements, 
# even if we try to call 20 of them this only returns values
# until we reach the last element
for value in ds.take(20):
    print(value)