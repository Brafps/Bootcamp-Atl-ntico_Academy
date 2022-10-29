from tensorflow import keras

model = keras.Sequential()

# Define the first dense layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Apply dropout to the first layer's output
model.add(keras.layers.Dropout(0.25))

# Define the output layer
model.add(keras.layers.Dense(4, activation='softmax', input_shape=(784,)))

# Compile the model
model.compile(optimizer = 'adam', loss='categorical_crossentropy')

# Print a model summary
print(model.summary())