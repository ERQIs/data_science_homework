import tensorflow as tf
from tensorflow.keras.datasets import mnist

def lenet5_model(input_shape, num_classes):
    model = tf.keras.models.Sequential([
        tf.keras.layers.UpSampling2D(size=(2, 2), input_shape=input_shape),
        tf.keras.layers.Conv2D(6, kernel_size=(5, 5), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(16, kernel_size=(5, 5), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(120, activation='relu'),
        tf.keras.layers.Dense(84, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model


# 加载MNIST数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 只使用部分数据，可以根据需要进行调整
subset_size = 1000
x_train = x_train[:subset_size]
y_train = y_train[:subset_size]
x_test = x_test[:subset_size]
y_test = y_test[:subset_size]

# 数据预处理：将像素值缩放到0到1之间，并将图像大小调整为32x32
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# 将标签转换为one-hot编码
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

# 构建 LeNet-5 模型
model = lenet5_model((28, 28, 1), 10)

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_test, y_test))

# 评估模型
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy)
