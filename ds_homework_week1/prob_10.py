s = input("input a string: ")
last_c = chr(0)
flag = 0
for c in s:
    if (c == last_c):
        print("包含连续字符组成的字符串")
        flag = 1
        break
    else:
        last_c = c
if flag == 0:
    print("不包含连续字符组成的字符串")
