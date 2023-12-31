import tensorflow as tf

x1 = tf.RaggedTensor.from_row_splits(
    values=[1, 2, 3, 4, 5, 7, 8, 9, 10],
    row_splits=[0, 5, 9])
print('x1: ',x1)

x2 = tf.RaggedTensor.from_row_splits(
    values=[1, 2, 3, 4, 5, 7, 8, 9, 10],
    row_splits=[0, 4, 7, 9])
print('x2: ',x2)

x3 = tf.RaggedTensor.from_row_splits(
    values=[1, 2, 3, 4, 5, 7, 8],
    row_splits=[0, 4, 4, 6, 7, 7])
print('x3: ',x3)
