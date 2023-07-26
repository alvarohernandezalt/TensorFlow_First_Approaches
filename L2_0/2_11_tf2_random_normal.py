import tensorflow as tf

# initialize a 6x3 2nd order tensor of random numbers
values = {'weights':tf.Variable(tf.random.normal([6,3]))}

print('Values:')
print(values['weights'])
