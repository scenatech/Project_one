my_string = "Hello, world ! This is a test string"

# print(len(my_string))

# m = my_string
# # print(len(m))

substring = my_string[0:3]
print(substring)

subs_end = my_string[33:]

print(subs_end)

# my_string = "Hello, world ! This is a test string".upper()
# print(my_string)

# my_string = "Hello, world ! This is a test string"
# modi_my_string = my_string.replace(" "," - ")
# print(modi_my_string)

# if my_string.startswith ("Hello"):
#     print(True)
# else:
#     print(False)

# word_list = my_string.split()
# print(word_list)

# if "world" in my_string:
#     print(True)
# else:
#     print(False)

# #2
# my_int = 120
# print(my_int)

# my_float = 2.0
# print(my_float)

# my_list = ['francis','ama','fred']
# for nam in my_list:
#     print(nam)

# my_tuple = ('ama','kofi','sena')
# for sen in my_tuple:
#     print(my_tuple)

#3
my_int = 25
print(my_int)
my_int += 10
print(my_int)
# my_int = 25
my_float = float(my_int)
print(my_float)

another_int = 5
my_int = 30
sum_result = (another_int + my_int)
print(sum_result)

div_result = (my_int / another_int)
print(div_result)

# #4
# my_float = 150.50
# print(my_float)

# my_float = 35.50
# increase_by = 1.5
# my_float = (my_float + increase_by)
# print(my_float)

# my_float = 35.50
# my_int = int(my_float)
# print(my_int)

# another_float = 50.50

# product_result = (my_float * another_float)
# print(product_result)

# div_result = (another_float / my_float)
# print(div_result)

# #5
# my_list = ['koda','bebe','flash','etor']
# for nam in my_list:
#     print(nam)

# my_list.append('oheneba')
# print(my_list)

# my_list = ['koda','bebe','flash','etor','oheneba']
# print(my_list[2])


# my_list[3] = 'dzato'
# print(my_list)

# if 'flash' in my_list:
#     print(True)
# else:
#     print(False)

# my_list.remove('koda')
# print(my_list)

# my_list = ['bebe','flash','dzata','oheneba']

# #6
# my_tuple = ('lovlyn','grace','bella','bibi')
# for ladies in my_tuple:
#     print(ladies)

# print(my_tuple[1])

# if 'bella'in my_tuple:
#     print(True)
# else:
#     print(False)

# print(my_tuple[2])

# my_tuple = ('lovlyn','grace','bella','bibi')
# my_list = (['lovlyn','grace','bella','bibi'])
# print(my_list)

# my_list.append('grace')
# print(my_list)

# new_tuple = tuple(my_list)
# print(new_tuple)

# new_tuple = ('lovlyn','grace','bella','bibi','grace')
# for lad in new_tuple:
#     print(lad)

# my_range = range(1,11)
# for num in my_range:
#     print(num)

# print(len(my_range))

# value = 15
# if value in my_range:
#     print(True)
# else:
#     print(False)

# new_range = range(10,0,-1)
# for num in new_range:
#     print(num)

# my_dict = {'name':'Francis','age':33,'City':'Canada'}
# print(my_dict)

# my_dict = dict(name = 'Felix',age = 35,City = 'USA')
# print(my_dict)

# print(my_dict['name'])

# my_dict['age'] = 45
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# fruits = ['apple','banana','cherry']
# for fruit in fruits:
#     print(fruit)

# message = 'Hello,world!'
# for char in message:
#     print(char)

# range = range(1,6)
# for num in range:
#     print(num)


# name = input('what is your name?: ')
# age = int(input('Please enter your age: '))
# print(name,age)

# name = 'Felix'
# age = 45
# result = ('his name is '   +   name   +  ' and he is '  +  str(age)   +  'years old')
# print(result)

# name = input('Please enter your name: ')
# age = int(input('Please enter your age:  '))
# result = ('welcome' + name + ' and i am ' + str(age) + ' years old ') 
# print(result)

# # grocery_store = ['mango','juice','pineapple','apple']
# # grocery_store.append('banana')
# # print(grocery_store)

# grocery_store = []

# user1 = int(input('Please enter the number of fruit:  '))
# user2 = input('Please enter your choice of fruit: ')

# grocery_store.append(user1)
# grocery_store.append(user2)

# courses = ('Maths','Physics','Chemistry','Chemistry')
# print(courses[0])

# print(courses.count('Chemistry'))

# a = [('kofi','ama')]

# a.insert(1,"kenn")
# print(a)

items = ['mango','orange','tomatoes']

hold = []

user = input('Please add your choice of fruit: ')

items.append(user)
print(items)

print(items[1:])

empty = items[1:]

result = hold.append(empty)
print(result)

for i in range(start,end + 1):
    total += i
print(f'the sum of numbers from {start} to {end} is {total}')






















