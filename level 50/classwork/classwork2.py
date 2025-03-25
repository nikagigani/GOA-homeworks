try:
    user_input = input("Please enter your name or surname: ")
    print(f"Hello, {user_input}!")
except Exception as a:
    print(f"An error occurred: {a}")