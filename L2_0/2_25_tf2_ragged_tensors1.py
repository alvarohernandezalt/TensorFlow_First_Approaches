# ragged tensor are the one that are not linear
# usually tensor lacks of some data (as in reality)
# lets see how iterate with them

import tensorflow as tf

digits = tf.ragged.constant([[3, 1,4,1], [], [5,9,2], [6],[]])
words = tf.ragged.constant([['Bye', 'now'], ['Thank', 'you', 'again', 'sir']])

print(tf.add(digits, 3))