from sklearn import datasets

def distance(a, b):
    return (sum((a - b) * (a - b)))**0.5

iris = datasets.load_iris()
X = iris.data
y = iris.target

datas = [[], [], []]

# 分类三种数据
for i in range(len(y)):
    clas = y[i]
    datas[clas].append(X[i])
    

# 求平均向量
mean = []
for clas in range(3):
    mean.append(sum(datas[clas])/len(datas[clas]))

print(mean)
print(distance(mean[0], mean[1]))

for clas in range(3):
    print("类型{}的中心点为{}".format(clas, mean[clas]))
    for i in range(len(datas[clas])):
        print( "样本点{} : {}, 到中心点的距离 {}".format(i, datas[clas][i], distance(datas[clas][i], mean[clas])  ) ) 
