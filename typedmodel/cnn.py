#imports
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

#initlaize model config

def model_config(train_images, test_images, train_formulas, test_formulas):
    train_images, test_images = train_images / 255.0, test_images / 255.0

    # go up to block 3
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(250, 500, 2)))
    model.add(layers.MaxPooling2D((2, 2)))
