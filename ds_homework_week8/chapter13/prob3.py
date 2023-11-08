from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
data = load_iris()
features = data.data
target = data.target

# 划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 创建KNN分类器对象
knn = KNeighborsClassifier()

# 在训练集上训练KNN分类器
knn.fit(X_train, y_train)

# 对训练集进行预测并计算准确度
train_accuracy = knn.score(X_train, y_train)
print("训练集准确度：", train_accuracy)

# 对测试集进行预测并计算准确度
test_accuracy = knn.score(X_test, y_test)
print("测试集准确度：", test_accuracy)
