#✅ Variable
#✅ Comments
#✅ String
#✅ Int
#✅ Float
#✅ List
#✅ Tuple
#✅ Range
#✅
#✅

#Example 1

# ✅Printing anything general using print function
print("Hello world")
print('The headmaster was not in class last time')
# --------------------------------------------------------------

# Example 2
# ✅Using VARIABLE
students2 ='benjamin,mavis'
students3 ="kwame,godwin"
# --------------------------------------------------------------


# Example 3
# ✅using a DESCRIPTIVE name
grocery_store = 'fruit juice,mango'
grocery_store2 = ("banana, orange")
# --------------------------------------------------------------

# ✅Example 4
AGE = 24
# --------------------------------------------------------------


#Example 5
kofi_store = ('banana','mango','apple','watermelon')
ama_store =('pineapple','guava','apple','orange')
# --------------------------------------------------------------


#✅Data types with examples
age = 22 #int data type

kofi_is_a_male = True #boolean data type

price_of_gari = 22.00 #float data type
# --------------------------------------------------------------


hobby =('sena likes gardening') #string data type

store = {'rice': 22,'oil':1} #dict data type

grocery_store = ['mango','apple','kiwi'] #list data type

students_attributes = ('male',22,25.5,'fisrt_class','lecturers') #tuple data type
# --------------------------------------------------------------

#✅This program takes user input and print on console
name = input('what is your name: ') 
age = int(input('please enter your age: '))
# print(name,age)
# --------------------------------------------------------------


#✅This program concatenates two inputs(hard code)
name = 'sena' 
age = 18

result = ('my name is '+ name+ ' and i am '+ str(age)+' years old')
# --------------------------------------------------------------


#✅This program takes user inputs and concatenates it
name = input('please enter your name: ')
age = int(input("please enter your age: "))

result = ('Welcome '+ name+ ' and i am '+ str(age)+' years old')
# --------------------------------------------------------------


#✅This program takes Int and Float value(Hard code)
first_number = 22
second_number = 22.3

final_answer =first_number + second_number
# --------------------------------------------------------------

#✅This program takes Int and Float value from a user
first_number = int(input('please enter your first number: '))
second_number =float(input('please enter your second number: '))

result = ('your final answer is ' + str(first_number + second_number))
print(result)
# --------------------------------------------------------------

#✅How to check for the type of built in data type
#Example 
my_list = [2,3,4]
print(type(my_list))
# --------------------------------------------------------------

#✅How to check for the attributes of built in data types
#Example
print(dir(my_list))
# --------------------------------------------------------------

#✅How to use append data type to add to a list(hard code)
grocery_store = ['mango', 'juice','pineapple','apple']
# my_list2 = ('kofi','ama')


grocery_store.append('banana')
print(grocery_store)
# --------------------------------------------------------------


#✅How to use append data type to add to a list
grocery_store = ['mango', 'juice','pineapple','apple']
# my_list2 = ('kofi','ama')

user = input('please enter your choice of fruit: ')

grocery_store.append(user)
print(grocery_store)
# --------------------------------------------------------------


#✅How to use .append and input to get user input
grocery_store = []


user2 =int(input('Please enter the number of fruit: '))
user = input('Please enter your choice of fruit: ')


grocery_store.append(user2)
grocery_store.append(user)


print(grocery_store)
#-----------------------------------------------------------
 #✅How to use insert,index, and clear attributes 
grocery_store = ['mango','juice','pear']

grocery_store.insert(1,'kiwi')

user = input('Please enter your choice of fruit: ')

grocery_store.insert(1,user)

grocery_store.clear()

print(grocery_store.index('juice'))

grocery_store.pop(3)

print(grocery_store)




grocery_store = ['mango', 'juice','pineapple','apple']
#✅Attributes of List
"""
count,extend,index,insert,pop,
remove,reverse,sort,clear,copy
append,

"""

#Example two
#grocery_store[2] returns a single element from the list at index 2,while 
#grocery_store[2:]returns a new list containing a subsequence of elements
#from the list starting at index 2 and going until the end of the list.

#--------------------------------------------------------------------------

# example 3

items = ['mango','orange','tomatoes']

hold =[]

user = input('Please add your choice of fruit: ')

items.append(user)
print(items)

print(items[1:])

empty = items[1:]

result = hold.append(empty)
print(result)
# ------------------------not done---???



grocery_store.append('strawberry')
grocery_store.insert(3, 'juice')
grocery_store.clear()
print(grocery_store.index('mango'))
grocery_store.pop(1)
grocery_store.remove('apple')
grocery_store.reverse()
grocery_store.sort()
print(grocery_store.count('pineapple'))
(grocery_store.extend('mango'))
grocery_store.copy()

# ------------------------------------------------




# Tuple
courses = ('Maths','Physics','Chemistry','Chemistry')

print(courses[0]) #accessing index

print(courses.count('Chemistry')) # checking for the number of times a values occurs

#-------------------------------------
#To mutate a tuple you have to change it to a list thus tuple in a list eg.

a = [('kofi','ama')]

a.inser(1,"kenn")
print(a)

user =int(input("Please enter your first number: "))

for i in range(1,user):
    print(i)





#using PRINT function to print students
# print(students2,students3)
# print(grocery_store)
# print(kofi_store,ama_store)
# print(kofi_store[1])
# print(ama_store[3])
print(result)
print(result)

