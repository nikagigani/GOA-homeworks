def manual_list(start, end, step, user_num):
    return [x for x in range(start, end, step,) if x >user_num]

print(manual_list(1, 2, 3, 4)) 
print(manual_list(10, 40, 11, 3)) 
print(manual_list(0, -17, 22, 8))