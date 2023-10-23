import numpy as np

vec_old = np.array([-1, 0])
vec_new = np.array([1, 0])

diff_norm = 1
accurence = 0.0001
step = 10

matrix = np.array([[2, 1],
                   [4, 5]])

while (diff_norm > accurence):
    vec_old = vec_new
    for i in range(step):
        vec_new = np.dot(matrix, vec_new)
    vec_new = vec_new / np.linalg.norm(vec_new)
    diff_norm = np.linalg.norm(vec_new - vec_old)

print("eigen vector:")
print(vec_new)

print("eigen value:")

idx = 0
while abs(vec_new[idx]) < accurence:
    idx += 1
    
print( np.dot(matrix, vec_new)[idx] / vec_new[idx] )
