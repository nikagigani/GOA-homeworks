def manual_find(main_string, str_to_find):
    result=-1

    for i in range(len(main_string)):
        if main_string[i] == str_to_find: result=i

    if result==-1:
        print("string index not found")
    else:
        print("result")