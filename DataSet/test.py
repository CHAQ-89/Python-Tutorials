year = int(input())
if (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)):
    print(True)
else:
    print(False)
