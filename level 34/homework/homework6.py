def positive_num(list):
    positive_numbers=[]
    for i in list:
        if i >=0:
            positive_numbers.append(i)
            print(positive_numbers)

positive_num([1,2,3,-1,21,32,-13,23,3])