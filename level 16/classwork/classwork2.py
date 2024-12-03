correct_password="GOA"
counter=0
user_guess=input("enter password: ")
while user_guess!=correct_password:
    user_guess=input("enter password: ")
    counter+=1
print("access granted")