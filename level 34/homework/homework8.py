def find_max(numbers):
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    print (max_number)


numbers = [10, 43, 22, 88, 5, 67]
print("The maximum number is:", find_max(numbers))