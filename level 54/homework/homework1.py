num1 = float(input("enter number: "))
num2 = float(input("enter number: "))

try:
    print(num1/num2)
except TypeError:
    print("wrong type")
except ValueError:
    raise ValueError("you cant devide with zero")
finally:
    print("Operation complete")