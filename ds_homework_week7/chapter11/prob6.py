from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

data = iris["data"]
target = iris["target"]

training_data, test_data, training_target, test_ans = train_test_split(data, target,test_size=0.3)

print("There are {} training samples".format(training_target.shape[0]))
print("There are {} testing samples".format(test_ans.shape[0]))
