def Cube_root():
    c = int(input("c = "))
    g = c/int(input("factor of g = "))
    i = 0
    while(abs(g*g*g -c) > 0.00000000001):
        g = (2*g + c/(g*g))/3
        i += 1
        print("%d:%.13f"%(i,g))
        
Cube_root()

# x_(n+1) = x - (x^3 - c)/(3x^2)
#         = (2x^3 + c)/(3x^2)
#         = (2/3)x + c/(3x^2)
#         = 1/3(2*x + c/x^2)
