import tensorflow as tf

x = tf.constant([100,200,300], name = 'x')
y = tf.constant([1,2,3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
prod_y = tf.reduce_prod(y, name='prod_y')
mean = tf.reduce_mean([sum_x,prod_y], name="mean")

print("sum_x: ", sum_x)
print("prod_y: ", prod_y)
print("mean: ", mean)