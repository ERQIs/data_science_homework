def myReverse_for(List):
    for i in range(len(List) - 1, -1, -1):
        print(List[i], end = ' ')
    print()
        
def myReverse_while(List):
    i = len(List) - 1;
    while(i >= 0):
        print(List[i], end = ' ')
        i -= 1
    print()


# the list to reverse is here
a = [1, 2, 3, 4, 5]


print("for edition:")
myReverse_for(a)
print("while edition:")
myReverse_while(a)
