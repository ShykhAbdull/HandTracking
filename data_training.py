from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator

# Your code using TensorFlow here

sz = 300
# Step 1 - Building the CNN

# Initializing the CNN
classifier = Sequential()

# First convolution layer and pooling
classifier.add(Conv2D(32, (3, 3), input_shape=(sz, sz, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Second convolution layer and pooling
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Flattening the layers
classifier.add(Flatten())

# Adding fully connected layers with dropout
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dense(units=9, activation='softmax'))  # softmax for more than 2

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # categorical_crossentropy for more than 2

# Step 2 - Preparing the train/test data and training the model
classifier.summary()

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('Handtracking/ASL_Data_set',
                                                 target_size=(sz, sz),
                                                 batch_size=32,
                                                 color_mode='rgba',
                                                 class_mode='categorical')

history = classifier.fit(
    training_set,
    steps_per_epoch=10,  # No of images in the training set
    epochs=30,  # Increase epochs for better convergence
)


# Saving the model
model_json = classifier.to_json()
with open("Handtracking/Model/model_weights", "w") as json_file:
    json_file.write(model_json)
print('Model Saved')
classifier.save_weights('model-bw.h5')
print('Weights saved')
