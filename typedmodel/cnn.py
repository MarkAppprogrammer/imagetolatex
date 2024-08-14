#imports
import tensorflow as tf

#initlaize model config

class ResNetBlock:
    def __init__(self, out_channels):
        self.conv_seq  = tf.keras.Sequential([
            tf.keras.layers.Conv2D(
                filters=out_channels, 
                kernel_size=(3, 3), 
                padding='same', 
                input_shape=(250, 500, 2)
            ),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Activation('relu'),
            tf.keras.layers.Conv2D(
                filters=out_channels, 
                kernel_size=(3, 3), 
                padding='same', 
                input_shape=(250, 500, 2)
            ),
            tf.keras.layers.BatchNormalization()
        ])

        self.extrapass = tf.keras.Sequential([
            tf.keras.layers.Activation('relu')
        ])
    
    def call(self, inputs):
        x = self.conv_seq(inputs)

        #skip connect
        #add stuff to fix dimensions
        if x.shape == inputs.shape:
            x = x + inputs

        return self.extrapass(x)

class ResNetModel:
    def __init__(self):
        super(ResNetModel, self).__init__()

        self.begginer = tf.keras.Sequential([
            tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=(7, 7),
                padding="same",
                input_shape=(250, 500, 2),
                strides=(2,2)
            ),
            tf.keras.layers.Activation('relu'),
            tf.keras.layers.GlobalMaxPool2D(data_format="channels_last")
        ])

        self.blocks = tf.keras.Sequential([
            ResNetBlock(64),
            ResNetBlock(64)

            #3 blocks now change of dimensions
        ])

def model_config(train_images, test_images, train_formulas, test_formulas):
    # go up to block 3
    print("not done yet")
    

    
