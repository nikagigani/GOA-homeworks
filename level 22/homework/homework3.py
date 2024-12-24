list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1=int(input("enter number: "))
num2=int(input("enter number: "))
if num1<num2:
    list1=list[num1:num2]
    print(list1)
elif num1>num2:
    list2=list[num2:num1]
    print(list2)
else: print([])