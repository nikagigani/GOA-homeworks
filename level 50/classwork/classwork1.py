num = 10
try:
    result = num + "string"
except TypeError as a:
    print(f"TypeError occurred: {a}")

print("everything is right")