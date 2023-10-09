def gcd(a, b):
    if a == b or b == 0:
        return a
    if a == 0:
        return b
    if a < b:
        b, a = a, b
    return gcd(b, a%b)

def main():
    a = int(input("a = (must be a positive integer): "))
    b = int(input("b = (must be a positive integer): "))
    if a < 0 or b < 0:
        print("invalid input")
        return
    print("the gcd of " + str(a) + " and " + str(b) + " is " + str(gcd(a, b)))


main()
