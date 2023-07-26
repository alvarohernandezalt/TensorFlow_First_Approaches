import tensorflow as tf

x = tf.constant([100,200,300], name = 'x')
y = tf.constant([1,2,3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
prod_y = tf.reduce_prod(y, name='prod_y')
div_xy = tf.math.divide(sum_x, prod_y, name="div_xy")

print("sum_x: ", sum_x)
print("prod_y: ", prod_y)
print("div_xy: ", div_xy)

