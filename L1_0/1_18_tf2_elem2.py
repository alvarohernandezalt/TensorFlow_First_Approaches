import tensorflow as tf 

arr2 = tf.constant([[1,2],[2,3]])

@tf.function
def compute_values():
    tf.print('arr2: ',arr2)
    arr_0 = arr2[0]
    tf.print('[0]: ',arr_0)
    print('[1]: ',arr2[1]) 

# Inside def, normal print in "eager" mode is always 
# the abstraction of the tensor as result
# And in the case of using tf.print() works inside a "def" 
# the same as if we use print(arr2.numpy()) outside tf.function

compute_values()