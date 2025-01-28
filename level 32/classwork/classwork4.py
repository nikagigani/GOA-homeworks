def manual_append(main_list, item_to_insert):
    length = len(main_list)
    main_list.insert(length, item_to_insert)
    print(main_list)

manual_append([1,2,3,4,5,6,7,8], 9)