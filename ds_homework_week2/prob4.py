def Square_root(n):
    for i in range(n):
        if i * i < n and (i + 1) * (i + 1) >= n:
            start = i
            break

    i = start
    while i < start + 1:
        if abs(i * i - n) <= 0.0001:
            return i
        i += 0.000001
    return 0

n = int(input("n = "))
print(Square_root(n))
