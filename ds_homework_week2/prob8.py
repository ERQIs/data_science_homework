from random import uniform
from time import time
from math import pi

def Pi_Monte_Carlo():
    print("Calculating Pi with method of Monte Carlo (to precison of 4 decimal place)... ")
    start_time = time()
    step = 10000 
    hit = 0
    for i in range(step):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if (x*x + y*y < 1):
            hit += 1
    shoot = step
    while abs(hit / shoot * 4 - pi) > 0.0001:
        for i in range(step):
            x = uniform(0, 1)
            y = uniform(0, 1)
            if (x*x + y*y < 1):
                hit += 1
        shoot += step
    
    end_time = time()
    print("result:" + str(4*hit/shoot) + " time used: " + str(end_time - start_time))

def Pi_Taylor_Formula_of_arcsin():
    print("Calculating Pi with method of Taylor Formula (to precison of 4 decimal place)... ")
    ret = 1
    x = 1
    i = 1
    step = 10000
    start_time = time()
    #for i in range(1, 200000000, 2):
    while abs(ret + ret - pi) > 0.0001:
        for k in range(step):
            x *= i
            x /= (i + 1)
            ret += x / (i + 2)
            i += 2
    end_time = time()
    print("result: " + str(ret * 2) + " time used: " + str(end_time - start_time))

def Pi_Machin_Formula(n):
    print("Calculating Pi with method of Machin Formula (to precison of " + str(n) + " decimal place)... ")
    start_time = time()
    t = n+10                                     #多计算10位，防止尾数取舍的影响
    b = 10**t                                    #为算到小数点后t位，两边乘以10^t
    x1 = b*4//5                                  #取整求含4/5的首项
    x2 = b // -239                               #取整求含1/239的首项
    s = x1+x2                                    #求第一大项
    n *= 2                                       #设置下面循环的终点，即共计算n项
    for i in range(3, n, 2):                     #循环初值=3，末值n,步长=2
        x1 //= -25                               #取整求每个含1/5的项及符号
        x2 //= -57121                            #取整求每个含1/239的项及符号
        x = (x1+x2) // i                         #求两项之和，除以对应因子，取整
        s += x                                   #求总和
    end_time = time()
    p = s*4                                     #求出π
    p //= 10**10                                #舍掉后十位
    print("result: " + str(p) + " time used: " + str(end_time - start_time))                               #输出圆周率π的值，不带小数点

Pi_Monte_Carlo()
Pi_Taylor_Formula_of_arcsin()
Pi_Machin_Formula(30)
