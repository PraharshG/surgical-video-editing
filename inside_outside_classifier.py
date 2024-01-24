import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

train_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_generator = train_data_gen.flow_from_directory(
    'datasets/train_images',
    target_size=(128, 128),  # Adjust the target size as needed
    batch_size=32,
    class_mode='binary'
)

model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Binary classification, so using sigmoid activation
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_generator, epochs=10)

#test_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
#
#test_generator = test_data_gen.flow_from_directory(
#    'path/to/test_dataset',
#    target_size=(128, 128),
#    batch_size=32,
#    class_mode='binary'
#)
#
#test_loss, test_acc = model.evaluate(test_generator)
#print(f'Test accuracy: {test_acc}')
#
model.save('in_out.h5')
