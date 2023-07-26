import tensorflow as tf
import numpy as np 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Create python array
array_1d = np.array([1.3,4.0,23.5])
tf_tensor = tf.convert_to_tensor(value=array_1d, dtype=tf.float64)

print(tf_tensor)
print(tf_tensor[0])
print(tf_tensor[1])