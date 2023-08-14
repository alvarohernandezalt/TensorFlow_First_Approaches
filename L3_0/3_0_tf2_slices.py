import tensorflow as tf

# combine the input into one element
t1 = tf.constant([[1, 2],[3, 4]])
ds1 = tf.data.Dataset.from_tensors(t1)

# separate element for each item
t2 = tf.constant([[1, 2],[3, 4]])
ds2 = tf.data.Dataset.from_tensor_slices(t2)
for item in ds1:
    print("1item: ", item)

print('--------------------------')

for item in ds2:
    print("2item: ", item)
