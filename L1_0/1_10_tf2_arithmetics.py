import tensorflow as tf

@tf.function # replace print with tf.print
def compute_values():
    a = tf.add(4,4)
    b = tf.subtract(8,6)
    c = tf.multiply (a, 3)
    d = tf.math.divide(a, 6)

    tf.print(a)
    tf.print(b)
    tf.print(c)
    tf.print(d)

compute_values()