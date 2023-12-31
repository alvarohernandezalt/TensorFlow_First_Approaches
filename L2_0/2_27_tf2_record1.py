import tensorflow as tf

data = b'pasta'
simple1 = tf.train.Example(features=tf.train.Features(
    feature={
        'my_ints' : tf.train.Feature(int64_list = tf.train.Int64List(value=[2, 5])),
        'my_float': tf.train.Feature(float_list = tf.train.FloatList(value=[ 3.6])),
        'my_bytes': tf.train.Feature(bytes_list = tf.train.BytesList(value=[data]))
    }
))
my_ints_value = simple1.features.feature['my_ints'].int64_list.value
print('my_ints:  ', simple1.features.feature['my_ints'], my_ints_value)

my_float_value = simple1.features.feature['my_ints'].float_list.value
print('my_float: ', simple1.features.feature['my_float'], my_float_value)

# print('my_bytes: ', simple1.features.feature['my_bytes'], bytes_list.value)

print(('simple1: ', simple1))