n = float(input("input the grade (be it a number from 0 to 100):"))
if n > 100 or n < 0:
    print("invalid input")
elif n >= 90:
    print("level 优秀")
elif n >= 75:
    print("level 良好")
elif n >= 60:
    print("level 合格")
else:
    print("level 不合格")
