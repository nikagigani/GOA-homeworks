user_number=int(input("enter natural number: "))
factorial, starting_number=1, 1

while starting_number<=user_number:
    print("starting_number:", str(starting_number))
    factorial*=starting_number
    print("factorial:", str(factorial))
    starting_number+=1
print("factorial of", str(user_number), "is:",str(factorial) )