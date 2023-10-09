def prefix_product(a):
    b = []
    la = len(a)
    if la == 0:
        return b
    b.append(a[0])
    lb = 1
    for i in range(la - 1):
        b.append(b[lb - 1] * a[i + 1])
        lb += 1
    return b

n = int(input("the length of the array(integer array): "))
a = []
for i in range(n):
    a.append( int(input("item number {:d}: ".format(i + 1))) )

print("array B:")
print(prefix_product(a))
