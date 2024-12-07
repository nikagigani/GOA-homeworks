correct_password="Goa best"
counter=0
user_input=input("Enter password: ")
while correct_password!=user_input:
    print("try again")
    user_input=input("Enter password: ")
    counter+=1
print(counter)