#Solutions to Test 1
#Question 1
my_string = "Ama's favorite food on sunday afternoon is Fufu"
print(my_string) #✅

#2
my_string = 'Happy day!'
print(len(my_string)) #✅

#3
my_string = "Happy day"
print(my_string[:3]) #✅

#4
my_string = "Happy day"
print(my_string[-3:]) #✅

#5
my_string = "Sena loves gardening".upper()
print(my_string) # -1 ✔️

# 6 NOT SURE ON ANSWER
my_string = "This mango really taste good"
new_string = my_string.replace()
print(my_string) #❌

# 7
my_string = "Hello world"
result = my_string.startswith("Hello")
print(result) # -1 ✔️

"""---------------------"""
my_string = "Hello world"
result = my_string.startswith("world",6,11)
print(result) # -1 ✅       

# #
my_string = "Hello world"
if "world" in my_string:
    print(True)
else:
    print(False) # -1 ✅
"""---------------------"""

# #8
my_string = "The food tastes good"
word_list = my_string.split()
print(word_list) # -1 ✅

# #9
my_string = "Hi,World"
contains_word = "World"in my_string
print(contains_word) # -1 ✅


"""_________Test 2 on Data Types Answers_____"""
# #1
my_int = 25
print(my_int) # ✅


# #2
my_float = 25.50
print(my_float) # ✅

# #3
my_list = ['strawberry','blue berry','star fruit'] # ✅

# #4
my_tuple = ('klenam','selorm','seyram','eyram') # ✅

#5 
my_range = range(1,11) # ✅


# #6 and 7
# #The answers are provided above (1 and 2)

# #8
my_list = ['strawberry','blue berry','star fruit']
for fruit in my_list:
    print(fruit) # ✅

# #9
my_tuple = ('klenam','selorm','seyram','eyram')
for grand in my_tuple:
    print(grand) # ✅

# #10
my_range = (1,11)
for elements in my_range:
    print(elements) # ✅

# """------Test 3:Python Integer Manipulation--------Ans """

# #1
my_int = 43 # ✅

# #2
my_int = 43
print(my_int) # ✅

# #3
my_int = 43
increase_by = 10
my_int = my_int + increase_by
print(my_int) # ✅
# #or
my_int = 43
increase_by = 10
my_int += increase_by
print(my_int) # ✅

#5 and 6
my_int = 25
my_float =float(my_int)
print(my_float) # ✅

# #7
another_int = 32 # ✅

# #8 and 9
another_int = 32
my_int = 15
sum_result = (another_int + my_int)
print(sum_result) # ✅

#10 and 11
my_int = 40
another_int = 2
div_result = my_int/another_int
print(div_result) # ✅

# """----Test 4-----Ans----Python Float M"""
# #1 and 2
my_float = 33.50
print(my_float) # ✅

#3 and 4
my_float = 33.50
increase_by = 1.50
my_float += increase_by
print(my_float)  # ✅

# #5 and 6
my_float = 33.50
my_int = int(33.50)
print(my_int)  # ✅

#7,8 and 9
nother_float = 25.50
my_float = 5.50  # ✅
# product_result = (another_float * my_float)
# print(product_result) 

#10 and 11
my_float = 25.50
another_float = 5.50
div_result = (my_float / another_float)
print(div_result)  # ✅

"""----Test 5 ----Python List Man.Ans----"""

#1 and 2
my_list = ['guava','pomogranade','kiwi']
for items in my_list:
    print(items)  # ✅

#3 and 4
my_list = ['guava','pomogranade','kiwi']
my_list.append('mango')
print(my_list)  # ✅
#5
my_list = ['guava','pomogranade','kiwi']
print(my_list[1])  # ✅

#6 and 7
my_list = ['guava','pomogranade','kiwi']
my_list[2] = 'apple'
print(my_list)  # ✅

#8---myway--to be explained--
my_list = ['guava','pomogranade','kiwi']
if items in my_list == list:
    print(True)
else:
    print(False)  # ✅

#8
my_list = ['guava','pomogranade','kiwi']
specific_value_to_check = 'guava'
if specific_value_to_check in my_list:
    print(True)
else:
    print(False)  # ✅

#9 and 10
my_list = ['guava','pomogranade','kiwi']
value_to_remove = 'pomogranade'
if value_to_remove in my_list:
    my_list.remove('pomogranade')
    print(my_list)

"""Test 6----Ans.Python Tuple Man.---"""
#1 and 2
my_tuple = ('kwame','kweku','kwadzo')
for name in my_tuple:
    print(name)  # ✅

#3
my_tuple = ('kwame','kweku','kwadzo')
print(my_tuple[1])  # ✅

#4
my_tuple = ('kwame','kweku','kwadzo')
specific_value = 'kwadzo'
if specific_value in my_tuple:
    print(True)
else:
    print(False)  # ✅

# #5
my_tuple = ('kwame','kweku','kwadzo')
print(my_tuple[2])  # ✅

#6
my_tuple = ('kwame','kweku','kwadzo')
my_list = (['kwame','kweku','kwadzo'])
print(my_list)  # ✅

#7
my_list = ['kwame','kweku','kwadzo']
my_list.append('kwesi')
print(my_list)  # ✅

#8 and 9
my_list = ['kwame','kweku','kwadzo','kwesi']
new_tuple = tuple(my_list)
for n in new_tuple:
    print(n)  # ✅

"""-----Test 7 Ans-Python Range Man____"""

#1
my_range = range(1, 11)

# #2
for num in my_range:
    print(num)  # ✅
    
# #3
print(len(my_range))


# #4 Check if a specific value exists in my_range
value = 0

if value in my_range:
    print(True)
else:
    print(False)  # ✅

#5
new_range = range(10 , 0 ,-1 ) 

#6
for num in new_range:
    print(num)  # ✅

#7
my_list = [10,9,8,7,6,5,4.3,2,1]

#8
print(my_list)  # ✅

