import tensorflow as tf

def lenet5_model(input_shape, num_classes):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(16, kernel_size=(5, 5), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(120, activation='relu'),
        tf.keras.layers.Dense(84, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model

# 输入图像大小为 32x32，通道数为 1
input_shape = (32, 32, 1)
# 分类的类别数，对于手写数字识别，类别数为 10
num_classes = 10

# 构建 LeNet-5 模型
model = lenet5_model(input_shape, num_classes)

# 输出模型的结构信息
model.summary()
