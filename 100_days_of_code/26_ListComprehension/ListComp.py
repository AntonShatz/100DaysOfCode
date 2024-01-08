list = [1, 2, 3]
new_num = [n + 2 for n in list]

name = " Jinx "
new_letter_list = [n for n in name]
print(new_num)
print(new_letter_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ["er", "ra", "shabu", "lamer"]

short_names = [name for name in names if len(name) < 3]
print(short_names)

long_names = [x.upper() for x in names if len(x)>2]
print(long_names)

#Squaring numbers
numbers = [1,1,2,3,4,8,13,21,34,55]
new_nums = [num*num for num in numbers]
print(new_nums)

#Filtering even numbers
list_of_string = ('1,1,3 ,3, 2, 1,2 ,123,13').split(',')
numbers = [int(x) for x in list_of_string]
result = [x for x in numbers if x%2==0]
print(result)

# Data overlap
print('-'*50)
numbers_1 = [1,1,2,3,4,8,13,21,34,55]
numbers_2 = [11,21,2,32,24,83,13,231,34,8,55,1]
result_2 = [num for num in numbers_1 if num in numbers_2]
print(result_2)

