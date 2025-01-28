def generate_big_sentence(name, surname, age):
    print(f"my name is {name}, my surname is {surname}, my age is {age}.")


name = input("enter your name: ")
surname = input("enter your surname: ")
age = int(input("enter your age: "))


generate_big_sentence(name, surname, age)