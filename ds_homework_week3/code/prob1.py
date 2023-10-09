def small_to_bin(small):
    result = ""
    while (small > 0):
        small *= 2
        result += "01"[int(small)]
        small -= int(small)
    return result

n = float(input("n = "))
minusFlag = 0
if (n < 0):
    minusFlag = 1
    n = -n
    
big = int(n)
small = n - big

if (minusFlag):
    print("-", end = '')
print(bin(big)[2:], small_to_bin(small), sep = '.')
