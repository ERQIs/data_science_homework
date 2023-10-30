print("importing library...")

import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
# 加载鸢尾花数据集
from sklearn.datasets import load_iris


print("handling data...")
iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)


# 将目标变量转换为独热编码
#target = tf.keras.utils.to_categorical(y_train)
target = np.argmax(target, axis=1)
print("constructing model...")
# 构建神经网络模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

print("compiling model...")
# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print("training model...")
# 训练模型
model.fit(X_train, y_train, epochs=10, batch_size=32)

print("pridicting...")
# 使用模型进行预测
predictions = model.predict(X_test)

print("testing...")
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy*100:.2f}%")
