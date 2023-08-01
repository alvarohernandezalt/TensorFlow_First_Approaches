import tensorflow as tf
import os

checkpoint_dir = 'C:/Users/ÁlvaroHernández/Documents/GitHub/TensorFlow_First_Approaches/L2_0'
os.makedirs(checkpoint_dir, exist_ok=True)

x = tf.Variable(10.)
# Checkpoint = tf.train.Checkpoint()
checkpoint = tf.train.Checkpoint(x=x)
print('x: ',x)

# assign a new value to x and save
x.assign(3.)
print('x: ',x)
checkpoint_path = os.path.join(checkpoint_dir,'ckpt')
checkpoint.save(checkpoint_path)

# change the variable after saving
x.assign(25.)
print('x: ',x)

# restore values from the checkpoint
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))
print('x: ',x)