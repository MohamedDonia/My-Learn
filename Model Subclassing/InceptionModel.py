import tensorflow as tf

tf.keras.backend.clear_session()

class ConvModule(tf.keras.layers.Layer):
    def __init__(self, filters, kernel_size, strides, padding='same'):
        super(ConvModule, self).__init__()
        self.conv = tf.keras.layers.Conv2D(filters=filters,
                                           kernel_size = kernel_size, 
                                           strides=strides,
                                           padding=padding)
        self.bn = tf.keras.layers.BatchNormalization()

        
    def call(self, input_tensor, training=False):
        x = self.conv(input_tensor)
        x = self.bn(x, training=training)
        x = tf.keras.activations.relu(x)
        # x = tf.nn.relu(x)
        return x
    

cm = ConvModule(96, (3,3), (1,1))
y = cm(tf.ones(shape=(2,32,32,3))) # first call to the `cm` will 
print("weights:", len(cm.weights))
print("trainable weights:", len(cm.trainable_weights))


class InceptionModule(tf.keras.layers.Layer):
    def __init__(self, kernel_size1x1, kernel_size3x3):
        super(InceptionModule, self).__init__()
        # two conv modules: 
        self.conv1 = ConvModule(filters=kernel_size1x1,
                                kernel_size=(1,1),
                                strides=(1,1))
        self.conv2 = ConvModule(filters=kernel_size3x3,
                                kernel_size=(3,3),
                                strides=(1,1))
        self.cat = tf.keras.layers.Concatenate()
        
    def call(self, input_tensor, training=False):
        x_1x1 = self.conv1(input_tensor)
        x_3x3 = self.conv2(input_tensor)
        x = self.cat([x_1x1, x_3x3])
        return x


im = InceptionModule(96, 64)
y1 = im(y) # first call to the `cm` will 
'''
The main intuition for downsampling is that we hope to get more relevant feature information that highly 
represents the inputs to the model. As it tends to remove the unwanted feature so that model can focus on
the most relevant. There are many ways we can reduce the dimension of the feature maps (or inputs).
For example: using strides 2 or using the conventional pooling operation. 
There are many types of pooling operation, namely: MaxPooling, AveragePooling, GlobalAveragePooling.
'''

class DownSamplingModule(tf.keras.layers.Layer):
    def __init__(self, kernel_size):
        super(DownSamplingModule, self).__init__()
        self.