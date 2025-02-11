def no_duplicates(user_list):
    return list(set(user_list))

print(no_duplicates([1,2,3,3,4,4,5,6]))
print(no_duplicates([1,2,True,3,4,4,True,5,6]))
print(no_duplicates([1,"hello",3,3,4,"hello",5,6]))