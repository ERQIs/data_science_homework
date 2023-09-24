from math import sin
from random import uniform
def func(x):
    ret = 4 * sin(x) + x
    return ret * x

shoot = 10000000
hit = 0
for i in range(shoot):
    x = uniform(2, 3)
    y = uniform(0, 13)
    if (y < func(x)):
        hit += 1
        

print(13 * hit / shoot)
