''' 
Combining flat_map() and filter()

'''

import tensorflow as tf 
import numpy as np 

filenames = ['3_14_tf2_comments.txt']

ds = tf.data.Dataset.from_tensor_slices(filenames)

# 1) Use Datset.flat_map() to transform each file 
#    as a separate nested ds, then concatenate their
#    contents sequentially into a single "flat" ds
# 2) Skip the first line, the header-row
# 3) Filter out lines beginning with "#" (comments)

ds = ds.flat_map(
    lambda filename: (
        tf.data.TextLineDataset(filename)
        .skip(1)
        .filter(lambda line:
        tf.not_equal(tf.strings.substr(line, 0, 1), '#'))
    )
)

for values in ds:
    print(values)