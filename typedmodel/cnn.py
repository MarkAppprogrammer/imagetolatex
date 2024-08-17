import tensorflow as tf
tf.get_logger().setLevel('ERROR')

class ResNetBlock(tf.keras.layers.Layer):
    def __init__(self, out_channels, stride, downsample):
        super().__init__()
        self.downsample = downsample
        
        self.conv1 = tf.keras.layers.Conv2D(
            filters=out_channels,
            kernel_size=(3, 3),
            strides=(stride, stride),
            padding='same',
            use_bias=False
        )
        self.b1 = tf.keras.layers.BatchNormalization()
        self.relu = tf.keras.layers.Activation('relu')
        
        self.conv2 = tf.keras.layers.Conv2D(
            filters=out_channels,
            kernel_size=(3, 3),
            padding='same',
            use_bias=False
        )
        self.b2 = tf.keras.layers.BatchNormalization()

        if self.downsample:
            self.downsample_layer = tf.keras.Sequential([
                tf.keras.layers.Conv2D(
                    filters=out_channels,
                    kernel_size=(1, 1),
                    strides=(stride, stride),
                    padding='same',
                    use_bias=False
                ),
                tf.keras.layers.BatchNormalization()
            ])
        else:
            self.downsample_layer = lambda x: x  # Identity function if no downsampling

    def call(self, inputs):
        shortcut = self.downsample_layer(inputs)
        x = self.conv1(inputs)
        x = self.b1(x)
        x = self.relu(x)
        
        x = self.conv2(x)
        x = self.b2(x)
        
        x += shortcut
        x = self.relu(x)
        
        return x

class ResNetModel(tf.keras.Model):
    def __init__(self):
        tf.get_logger().setLevel('ERROR')
        super(ResNetModel, self).__init__()

        self.begginer = tf.keras.Sequential([
            tf.keras.layers.InputLayer(
                shape=(250, 500, 2)
            ),
            tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=(7, 7),
                padding="same",
                strides=(2, 2),
                use_bias=False
            ),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Activation('relu'),
            tf.keras.layers.MaxPooling2D(
                pool_size=(3, 3),
                strides=(2, 2),
                padding="same"
            )
        ])
        
        self.block1 = ResNetBlock(64, stride=1, downsample=False)
        self.block2 = ResNetBlock(128, stride=2, downsample=True)
        self.block3 = ResNetBlock(256, stride=2, downsample=True)
        
    def call(self, inputs):
        tf.get_logger().setLevel('ERROR')
        x = self.begginer(inputs)
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return x

    def model_config():
        model = ResNetModel()
        model.build((250, 500, 2))  
        #model.summary()

        return model

