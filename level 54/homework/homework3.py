user_input = input("enter number: ")

try:
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Please enter a valid number.")