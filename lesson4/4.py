list = [4, 7, 6, 4, 9, 1, 7, 1, 5, 3, 4]
print(list)
new_list = [i for i in list if list.count(i) == 1]
print(new_list)