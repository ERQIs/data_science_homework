import numpy as np
import matplotlib.pyplot as plt

np.random.seed(13)  # 设置随机种子，以便结果可复现

samples = np.random.randn(10000)

# x = np.arange(1, 101)  # 生成 x 坐标
y = samples  # 样本值作为 y 坐标

plt.hist(samples, bins=40, color='blue', alpha=0.7)  # 使用10个柱子绘制直方图
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Samples')
plt.grid(True)
plt.show()
