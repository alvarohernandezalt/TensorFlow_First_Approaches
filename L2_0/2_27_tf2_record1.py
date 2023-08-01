import tensorflow as tf

data = b'pasta'
simple1 = tf.train.Example(features=tf.train.Feature(
    feature={
        'my_ints' : tf.train.Feature(int66_list=tf.train.Int64List(value=[2, 5])),
        'my_float': tf.train.Feature(float_list=tf.train.FloatList(value=[3. 6])),
        'my_bytes': tf.train.Feature(bytes_list=tf.train.BytesList(value=[data]))
    }
))

