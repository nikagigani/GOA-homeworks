def max(num_list):
    max_value=num_list[0]

    for num in num_list:
        if num > max_value:
            max_value = num
    print(max_value)


max([1,2,3,4,10,6,7,8,9,5])