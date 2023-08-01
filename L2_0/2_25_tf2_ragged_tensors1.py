# ragged tensor are the one that are not linear
# usually tensor lacks of some data (as in reality)
# lets see how iterate with them

import tensorflow as tf

digits = tf.ragged.constant([[3, 1,4,1], [], [5,9,2], [6],[]])
words = tf.ragged.constant([['Bye', 'now'], ['Thank', 'you', 'again', 'sir']])

print(tf.add(digits, 3))
print(tf.reduce_mean(digits, axis=0))
print(tf.concat([digits, [[5, 3]]], axis=0))
print(tf.tile(digits, [1,2]))
print(tf.strings.substr(words, 0, 2))

