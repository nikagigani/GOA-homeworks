def delete(main_list, indexes_list):
    for i in indexes_list:
        main_list.pop(i)
    print(main_list)

delete([1,2,3,4,5,6,7,8], [4,2,4,2])