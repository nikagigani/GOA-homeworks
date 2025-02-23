def sum(start, end):
    total_sum=0
    for i in range(start, end+1):
        if i %3 ==0:
            total_sum +=i
    print(total_sum)
