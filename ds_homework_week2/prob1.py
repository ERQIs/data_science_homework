n = int(input("n = "))


def solution(n):
    
    if (n == 3):
        return n, 0, 1
    if (n == 2):
        return n, 0, 1
    if (n <= 1):
        return n, 0, 0
    
    twoes, threes = n//2, n % 2
    twoes -= threes
    ret = 0
    while twoes >= 0:
        # print("two " + str(twoes) + "  three " + str(threes) + " ret  " + str(ret))
        now = 1
        if (twoes > 0):
            now <<= twoes
        if (threes > 0):
            now *= 3**threes
        if (now > ret):
            ret = now
            twoesRec = twoes
            threesRec = threes
        threes += 2
        twoes -= 3
    return ret, twoesRec, threesRec

def solution_advanced(n):
    if (n <= 3):
        return n, 0, 0
    if (n % 3 == 0):
        twoes = 0
        threes = n//3
        return 3**threes, twoes, threes
    if (n % 3 == 1):
        twoes = 2
        threes = n//3 - 1
        return 4 * ( 3 ** threes), twoes, threes
    twoes = 1
    threes = n//3
    return 2 * (3 ** threes), twoes, threes



mul, twoes, threes = solution_advanced(n)

print("array containing " + str(twoes) + " twoes " + "and " + str(threes) + " threes")
print("the result:")
print(mul)
