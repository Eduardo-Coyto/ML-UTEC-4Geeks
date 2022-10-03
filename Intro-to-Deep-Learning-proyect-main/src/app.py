# Step 0. Load libraries and custom modules
# System --------------------------------------------------------
import os
import pathlib
# Dataframes and matrices ---------------------------------------
import numpy as np
import pandas as pd
# Graphics ------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Machine learning ----------------------------------------------
from sklearn.model_selection import train_test_split
# Deep learning -------------------------------------------------
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D,Dense,Dropout, Flatten 

from tensorflow.keras.layers import Activation, BatchNormalization
from tensorflow.keras.layers import MaxPooling2D 
from tensorflow.keras import datasets, layers, models 
from keras.utils import img_to_array
from keras.utils import get_file
from keras.utils import image_dataset_from_directory

# Sample a cat image
sample_cat = mpimg.imread('Pets/Cat/image3814.jpg') #vemos la imagen usando matplotlib
plt.imshow(sample_cat)
plt.show()

# Sample a dog image
sample_dog = mpimg.imread('Pets/Dog/image8941.jpg')
plt.imshow(sample_dog)
plt.show()

# Let's follow this tutorial: https://www.tensorflow.org/tutorials/load_data/images
# Create train dataset

# Las constantes por convencion las ponemos en mayuscula
IMAGE_WITDH = 200
IMAGE_HEIGHT = 200
BATCH_SIZE = 32


# Dividimos dataset en aprendizaje y validación
# En general se divide en 3 en tareas de deeplearning: train, validation y test

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(IMAGE_WITDH, IMAGE_HEIGHT),
  batch_size=BATCH_SIZE)

  # Create validation dataset
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2, #20% de validacion
  subset="validation",
  seed=123,
  image_size=(IMAGE_WITDH, IMAGE_HEIGHT),
  batch_size=BATCH_SIZE)

  # Create the deep learning architecture

# las imagenes a color tienen 3 canales: RGB
IMAGE_CHANNELS=3 
IMAGE_WIDTH=200
IMAGE_HEIGHT=200

model = Sequential([

Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)),
BatchNormalization(),
MaxPooling2D(pool_size=(2, 2)),
Dropout(0.25), 

Conv2D(64, (3, 3), activation='relu'),
BatchNormalization(),
MaxPooling2D(pool_size=(2, 2)),
Dropout(0.25),

Conv2D(128, (3, 3), activation='relu'),
BatchNormalization(),
MaxPooling2D(pool_size=(2, 2)),
Dropout(0.25),

Flatten(), 
Dense(512, activation='relu'),
BatchNormalization(),
Dropout(0.5),
Dense(1, activation='sigmoid'), 
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Fit the model
history=model.fit(train_ds, validation_data=val_ds, epochs=10)

# Guardar el Modelo
model.save('net_model_catdog.h5')

# Carga el modelo

loaded_model = keras.models.load_model('net_model_catdog.h5')

dog = mpimg.imread('cute_dog.jpg') #vemos la imagen usando matplotlib
plt.imshow(dog)
plt.show()

from keras.preprocessing import image
img = tf.keras.utils.load_img("dog.jpg",target_size=(200,200))
img = np.asarray(img)
plt.imshow(img)

# Predict
img_expanded = np.expand_dims(img, axis=0)
output = loaded_model.predict(img_expanded)
output