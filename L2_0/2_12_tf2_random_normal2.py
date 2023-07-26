import tensorflow as tf

for i in range(3):
    x_train = tf.random.normal((1,), mean=5, stddev=2.0)
    y_train = x_train * 2 + 3
    print('x_train: ',x_train)
print('----------------------\n')

for i in range(3):
    x_train = tf.random.normal((2,), mean=5, stddev=2.0)
    y_train = x_train * 2 + 4
    print('x_train: ',x_train)
print('----------------------\n')

for i in range(3):
    x_train = tf.random.normal((3,), mean=5, stddev=2.0)
    y_train = x_train * 2 + 6
    print('x_train: ',x_train)
print('----------------------\n')
