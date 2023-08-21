import tensorflow as tf

step = 20
rows = 100
slope = 0.4
bias = 1.5

x_train = tf.random.uniform(shape=(rows,))
perturb = tf.random.normal(shape=(len(x_train),), stddev=0.01)
y_train = slope * x_train + bias + perturb

# Initial values for slope 'm' and bias 'b'bias
m = tf.Variable(0.)
b = tf.Variable(0.)

# Predict the y value based on a value for x
def predict_y_value(x):
    y = m * x + b
    return y

# loss = RSS = residual sum of squares
#      = sum of squares of difference 
#        between predicted and true values
def squared_error(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))

loss = squared_error(predict_y_value(x_train), y_train)
print('Initial loss: ', loss.numpy())