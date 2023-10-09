import re
if (re.match("(^\d{15}$)|(^\d{17}([0-9]|x)$)", input("enter ID:")) == None):
    print("this is not an ID")
else:
    print("this could be an ID")
