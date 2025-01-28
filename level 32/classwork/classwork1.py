def generate_big_sentence(name, surname, age):
    print("my name is {}, my surname is {}, my age is {}.".format(name, surname, age))


name = input("enter your name: ")
surname = input("enter your surname: ")
age = int(input("enter your age: "))


generate_big_sentence(name, surname, age)