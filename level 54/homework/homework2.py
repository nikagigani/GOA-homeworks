list = [1,2,3,4,5]

try:
    print(list[7])
except IndexError:
    print("wrong index")