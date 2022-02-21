'''
in tf.keras, there is 3 ways we can define a neural network:
    -Sequential API
    -Functional API
    -Model Subclassing API
'''


import tensorflow as tf
import numpy as np

physical_devices_gpu = tf.config.list_physical_devices("GPU")[1]
physical_devices_cpu = tf.config.list_physical_devices("CPU")
tf.config.set_visible_devices([physical_devices_gpu] + physical_devices_cpu)
tf.config.experimental.set_memory_growth(physical_devices_gpu, True)

tf.keras.backend.clear_session()

input_dim = (28, 28, 3)
output_dim = 10

print(' '*40, '*'*40)
print(' '*40, ' '* 10, 'Sequential API')
print(' '*40, '*'*40)

# declare input shape
seq_model = tf.keras.Sequential()
seq_model.add(tf.keras.layers.Input(shape=input_dim, name="MyInput0")) 
# block 1
seq_model.add(tf.keras.layers.Conv2D(32, 3, strides=2, activation='relu',  name="MyInput"))
seq_model.add(tf.keras.layers.MaxPooling2D(3))
seq_model.add(tf.keras.layers.BatchNormalization())
# block 2
seq_model.add(tf.keras.layers.Conv2D(64, 3, strides=2, activation='relu'))
seq_model.add(tf.keras.layers.BatchNormalization())
seq_model.add(tf.keras.layers.Dropout(0.3))

# apply max pooling 
seq_model.add(tf.keras.layers.GlobalMaxPooling2D())
# out layer
seq_model.add(tf.keras.layers.Dense(output_dim, name='MyOutput'))

seq_model.summary()



print(' '*40, '*'*40)
print(' '*40, ' '* 10, 'Functional API')
print(' '*40, '*'*40)

input_ = tf.keras.layers.Input(shape = input_dim, name="MyInput0")
# block 1
x = tf.keras.layers.Conv2D(32, 3, strides=2, activation='relu', name="MyInput")(input_)
x = tf.keras.layers.MaxPooling2D(3)(x)
x = tf.keras.layers.BatchNormalization()(x)

# block2
x = tf.keras.layers.Conv2D(64, 3, strides=2, activation='relu')(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Dropout(0.3)(x)

gap = tf.keras.layers.GlobalAveragePooling2D()(x)
output = tf.keras.layers.Dense(output_dim, name="MyOutput")(gap)

# bind all
func_model = tf.keras.Model(input_, output)

func_model.summary()


print(' '*40, '*'*40)
print(' '*40, ' '* 10, 'Model SubClass API')
print(' '*40, '*'*40)

class ModelSubClassing(tf.keras.Model):
    def __init__(self, input_dim, num_classes):
        super(ModelSubClassing, self).__init__()
        # define all layers in the init
        self.input_dim_ = input_dim
        
        # layers of Block1
        
        self.conv1 = tf.keras.layers.Conv2D(32, 3, strides=2, activation='relu',name="MyInput")
        self.max1 = tf.keras.layers.MaxPooling2D(3)
        self.bn1 = tf.keras.layers.BatchNormalization()
        
        # layers of block2
        self.conv2 = tf.keras.layers.Conv2D(64, 3, strides=2, activation='relu')
        self.bn2 = tf.keras.layers.BatchNormalization()
        self.drop = tf.keras.layers.Dropout(0.3)
        
        # Gap. following by classifier
        self.gap = tf.keras.layers.GlobalAveragePooling2D()
        self.dense = tf.keras.layers.Dense(num_classes, name="MyOutput")
    
    def call(self, input_tensor, training=False):
        x = self.conv1(input_tensor)
        x = self.max1(x)
        x = self.bn1(x)
        
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.drop(x)
        
        x = self.gap(x)
        x = self.dense(x)
        return x
        
        
    def build_graph(self):
        x = tf.keras.layers.Input(self.input_dim_)
        return tf.keras.Model(inputs=[x], outputs=self.call(x))
    
    
    
sub_classing_model = ModelSubClassing(input_dim, output_dim)
sub_classing_model.build(input_shape=(None, *input_dim))
sub_classing_model.build_graph().summary()                         



(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# x_train.shape, y_train.shape: (60000, 28, 28) (60000,)
# x_test.shape,  y_test.shape : (10000, 28, 28) (10000,)

# train set / data 
x_train = np.expand_dims(x_train, axis=-1)
x_train = np.repeat(x_train, 3, axis=-1)
x_train = x_train.astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)

# test set / data 
x_test = np.expand_dims(x_test, axis=-1)
x_test = np.repeat(x_test, 3, axis=-1)
x_test = x_test.astype('float32') / 255
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)



# ----------------------------------------------------------------------------------- #
#                                        Compile
# ----------------------------------------------------------------------------------- #

# compile 
print('Sequential API')
seq_model.compile(
          loss      = tf.keras.losses.CategoricalCrossentropy(),
          metrics   = tf.keras.metrics.CategoricalAccuracy(),
          optimizer = tf.keras.optimizers.Adam())
# fit 
seq_model.fit(x_train, y_train, 
              batch_size=128, 
              epochs=10,
              validation_data=(x_test, y_test))

# compile 
print('\nFunctional API')
func_model.compile(
          loss      = tf.keras.losses.CategoricalCrossentropy(),
          metrics   = tf.keras.metrics.CategoricalAccuracy(),
          optimizer = tf.keras.optimizers.Adam())
# fit 
func_model.fit(x_train, y_train, 
               batch_size=128, 
               epochs=10,
               validation_data=(x_test, y_test))

#compile
print('\nSubclassing API')
sub_classing_model.compile(
          loss      =tf.keras.losses.CategoricalCrossentropy(),
          metrics   =tf.keras.metrics.CategoricalAccuracy(),
          optimizer = tf.keras.optimizers.Adam())
#fit
sub_classing_model.fit(x_train, y_train, 
                       batch_size=128, 
                       epochs=10,
                       validation_data=(x_test, y_test))