num=int(input("enter number: "))
is_valid=True
for i in range(2,num):
    if num%i==0:
        is_valid=False

if is_valid==True:print("your number is prime")
else:print("your number is not prime")