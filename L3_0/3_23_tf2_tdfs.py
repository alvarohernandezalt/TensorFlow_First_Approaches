''' 
Display available datasets from tensorflow_datasets package

'''

import tensorflow as tf 
import tensorflow_datasets as tfds 

# See available datasets
print(tfds.list_builders())

# Construct a tf.data.Dataset
ds = tfds.load(name="mnist", split=tfds.Split.TRAIN)

# Build your own pipeline
ds = ds.shuffle(1024).batch(32).prefetch(tf.data.experimental.AUTOTUNE)

for features in ds.take(1):
    image, label = features['image'], features['label']

