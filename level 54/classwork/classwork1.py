numerator = float(input("enter number: "))
denominator = float(input("enter number: "))

try:
    print(numerator/denominator)
except TypeError:
    print("wrong type")
except ValueError:
    raise ValueError("you cant devide with zero")
finally:
    print("Operation complete")