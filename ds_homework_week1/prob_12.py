def function_val(x, a, b, c, d):   # ax^3 + bx^2 + cx + d
    return a*x*x*x + b*x*x + c*x + d

def derivative_1(x, a, b, c, d):   # 3ax^2 + 2bx + c
    return 3*a*x*x + 2*b*x + c

def derivative_2(x, a, b, c, d):   # 6ax + 2b 
    return 6*a*x + 2*b

def delta(a, b, c):   # delta b^2 - 4ac for ax^2 + bx + c
    return b*b - 4 * a * c;

def NewtonIterate(x, n, a, b, c, d):    #对三次方程做n次牛顿法迭代
    for i in range(n):
        x = x - function_val(x, a, b, c, d) / derivative_1(x, a, b, c, d)
    return x
    

print("suppose the equation has the form of ax^3 + bx^2 + cx + d = 0, enter a, b, c, d:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

if (a == 0):    # 非三次方程
    if (b == 0):  # 非二次方程
        if (c == 0): # 无未知元
            if (d != 0):
                print("No solution for equation")
            else:
                print("Equation constant holds")
        else:      # 一次方程 cx + d = 0
            print("{:.5f}".format(- d / c))
    else:       #二次方程 bx^2 + cx + d = 0
        delt = delta(b, c, d)
        if (delt < 0):
            print("No solution for equation")
        elif (delt == 0):
            print("{:.5f}".format(-c/2*b))
        else:
            print("{:.5f} {:.5f}".format((-c + delt**0.5)/2*b, (-c - delt**0.5)/2*b))
else:    #三次方程
    delt = delta(3*a, 2*b, c) 
    if (delt <= 0):   #单调
        k = 0
        while(derivative_1(k, a, b, c, d) == 0):    #不能从极值点开始牛顿迭代，会导致除零
            k += 1
        print("{:.5f}".format(NewtonIterate(k, 300, a, b, c, d)))
    else:         #非单调
        
        extrema1 = (-2*b + delt ** 0.5)/(6*a)                                # 1 with right
        extrema2 = (-2*b - delt ** 0.5)/(6*a)    #三次函数的两个极值点           2 with left
        if (a < 0):
            extrema1, extrema2 = extrema2, extrema1

        extremaVal1, extremaVal2 = function_val(extrema1, a, b, c, d), function_val(extrema2, a, b, c, d)

        right, left, mid = extrema1 + 5, extrema2 - 5, (extrema1 + extrema2)/2
        
        if (extremaVal1 == 0):                  #零点出现在极值点处
            print("{:.5f} {:.5f}".format(NewtonIterate(left , 300, a, b, c, d), extrema1))
        elif (extremaVal2 == 0):
            print("{:.5f} {:.5f}".format(extrema2, NewtonIterate(right, 300, a, b, c, d)))

        elif ((extremaVal1 > 0) != (extremaVal2 > 0)):    #极值符号相反，有三个解
            print("{:.5f} {:.5f} {:.5f}".format(NewtonIterate(left, 300, a, b, c, d), NewtonIterate(mid, 300, a, b, c, d), NewtonIterate(right, 300, a, b, c, d)))

        else:              #极值符号相同，唯一解
            x = NewtonIterate(right, 300, a, b, c, d)
            if (function_val(x, a, b, c, d) != 0):
                x = NewtonIterate(left, 300, a, b, c, d)
            print("{:.5f}".format(x))

