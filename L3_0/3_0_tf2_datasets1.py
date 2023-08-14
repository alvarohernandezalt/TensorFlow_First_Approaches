import tensorflow as tf 

# Set random seed for testing the same data
tf.random.set_seed(37)

ds1 =  tf.data.Dataset.from_tensor_slices(
    (tf.random.uniform([3,2]), tf.random.uniform([3])))

ds2 =  tf.data.Dataset.from_tensors(
    (tf.random.uniform([3,2]), tf.random.uniform([3])))

print('---------------------------------------')
for i, item in enumerate(ds1):
    print('elem1: ' + str(i +1), item[0], intem[1])

print('---------------------------------------')
for i, item in enumerate(ds2):
    print('elem1: ' + str(i +1), item[0], intem[1])

print('---------------------------------------')
