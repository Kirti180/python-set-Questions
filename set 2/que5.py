def add_lists(list1, list2):
    new_list = []
    length = min(len(list1), len(list2))
    
    for i in range(length):
        new_list.append(list1[i] + list2[i])
    
    if len(list1) > length:
        new_list.extend(list1[length:])
    elif len(list2) > length:
        new_list.extend(list2[length:])
    
    return new_list

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result_list = add_lists(list1, list2)
print(result_list)
