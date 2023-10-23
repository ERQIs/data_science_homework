import numpy as np

matrix = np.array([[2, 1],
                   [4, 5]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("特征向量：")
for vector in eigenvectors.T:
    print(vector)

print("特征值：")
print(eigenvalues)

