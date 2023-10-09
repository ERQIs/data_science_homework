def direct_sort(a):
    la = len(a)
    if (la <= 1):
        return
    for i in range(1, la):
        pos = i - 1
        now = a[i]
        while pos >= 0 and a[pos] > now:
            a[pos+1] = a[pos]
            pos -= 1
        a[pos + 1] = now
            


n = int(input("the length of the array(integer array): "))
a = []
for i in range(n):
    a.append( int(input("item number {:d}: ".format(i + 1))) )

direct_sort(a)

print(a)

