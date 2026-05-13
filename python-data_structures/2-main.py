#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]

print(replace_in_list(my_list, 3, 9))
print(replace_in_list(my_list, -1, 7))
print(replace_in_list(my_list, 10, 8))
print(my_list)
