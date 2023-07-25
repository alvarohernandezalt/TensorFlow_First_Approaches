import tensorflow as tf 

# Create a 6x3x4 tensor of random numbers
values = {'weights':tf.Variable(tf.random.normal([6,3,4]))}

print('values:')
print(values['weights'])