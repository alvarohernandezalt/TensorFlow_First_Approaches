import tensorflow as tf

for i in range(3):
    x_train = tf.random.normal((1,), mean=5, stddev=2.0)
    y_train = x_train * 2 + 3
    print('x_train: ',x_train)
print('----------------------\n')

