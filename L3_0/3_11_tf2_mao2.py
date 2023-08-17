import tensorflow as tf 
import numpy as np

# Simple numpy array
x = np.array([[1],[2],[3],[4]])

# Make a dataset from a NumPy array
dataset = tf.data.Dataset.from_tensor_slices(x)

# METHOD #1: THE LONG WAY
# a lambda expression to double each value
# dataset = dataset.map(lambda x: x*2)
# a lambda expression to add one
# dataset = dataset.map(lambda x: x+1)
# a lambda expression to cube each value
# dataset = dataset.map(lambda x: x**3)

# METHOD #2: THE SHORT WAY
dataset = dataset.map(lambda x: x*2).map(lambda x: x+1).map(lambda x: x**3)

# METHOD #3: THE SHORTEST WAY (THE BOOK DON'T SAY ABOUT IT)
# Just doing some simple math inside the lambda expession
dataset2 = dataset.map(lambda x: ((2*x)+1)**3)

# testing and comparing that they are the same values
for values in dataset:
    print('values: ', values)

for values in dataset2:
    print('values: ', values)

