def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("n = "))
if isPrime(n):
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
