import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# price of pasta per kilogram
df = pd.read_csv('4_7_pasta.csv', index_col=0)

weight = df['weight']
price = df['price']

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

# MSE loss function and Adam optimizer
model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.adam(0.1))

# Train the model
history = model.fit(weight, price, epochs=100, verbose=False)

# Graph the # of epochs versus the loss
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.plot(history.history['loss'])
plt.show()

print('Cost for 11kg: ', model.predict([11.0]))
print('Cost for 45kg: ', model.predict([45.0]))