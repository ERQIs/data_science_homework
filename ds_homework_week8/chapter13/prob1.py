import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
data = load_iris()
features = data.data
target = data.target
target_names = data.target_names

# 可视化数据
for i in range(features.shape[1]):
    for j in range(features.shape[1]):
        if i != j:
            plt.scatter(features[:, i], features[:, j], c=target)
            plt.xlabel(data.feature_names[i])
            plt.ylabel(data.feature_names[j])
            plt.title('Iris Dataset')
            plt.show()
