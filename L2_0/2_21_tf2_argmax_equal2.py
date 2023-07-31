import tensorflow as tf
import numpy as np

# predictions from our model
pred = np.array ([[0.1, 0.03, 0.2, 0.05, 0.02, 0.6],
                  [0.5, 0.04, 0.2, 0.06, 0.10, 0.1],
                  [0.2, 0.04, 0.5, 0.06, 0.10, 0.1]])
                
# true values from our labeled data:
y_vals = np.array ([[0,  0,  0,  0,  0,  1],
                    [1,  0,  0,  0,  0,  0],
                    [0,  0,  1,  0,  0,  0]]])

print('argmax(pred,1): ', tf.argmax(input=pred, axis=1))
print('argmax(y_vals,1): ', tf.argmax(input=y_vals, axis=1))