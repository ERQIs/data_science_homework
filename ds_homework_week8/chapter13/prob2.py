from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
data = load_iris()
features = data.data
target = data.target

# 划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 打印训练集和测试集的大小
print("训练集大小：", X_train.shape)
print("测试集大小：", X_test.shape)
