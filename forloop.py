"""🚨📑Case_study and `examples 1` """


#✅ Assigning a string to a variable
my_string = "Hello, World!"


#✅ Assigning a tuple to a variable
my_tuple = ('mango', 'banana', 'orange')


#✅ Assigning a list to a variable
my_list = ['kiwi', 'mango', 'orange']


#-------------------✅---------------------------
for char in my_string:
	print(char)
print()


for item in my_tuple:
	print(item)
print()


for items in my_list:
	print(items)
#------------------------------------------------


#-------------------✅---------------------------
for char, string in enumerate(my_string):
	print(char, string)
print()


for char, string in enumerate(my_tuple):
	print(char, string)

print()


for char, string in enumerate(my_list):
	print(char, string)
#-------------------✅---------------------------


#-------------------✅---------------------------
for i in range(len(my_string)):
	print(my_string[i]) 
	"""# The len() function returns the length of the string my_string. In this case, 
	it returns the total number of characters in the string.

	my_string[i]: Within each iteration, my_string[i] accesses the character at index i in the string my_string. 
	The value of i changes in each iteration, allowing access to each character of the string.
	"""

for j in range(len(my_tuple)):
	print(my_tuple[j])

print()

for t in range(len(my_list)):
	print(my_list[t])
#-------------------✅---------------------------


"""---------------🚨`examples 2`---------------------"""
#✅ Assigning a dictionary to a variable
students_names = {
	"name": 28,
	"ben": 27,
	"vivian": 21,
	"gidoen": 26
}


result = students_names.items()
result = students_names.keys()
result = students_names.values()
result = students_names.get('course')
result = students_names.update({"country": 'usa'})
result = students_names.pop('age')
result = students_names.clear()
result = students_names.copy()
result = dict.fromkeys(students_names, '')
result = students_names.popitem()
result = students_names.setdefault('tech', 'kenn')


"""
'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values']
"""

#-------------------✅---------------------------
start = 1
end = 10
total = 0


for i in range(start, end + 1):
	total += i
print(f'the sum of numbers from {start} to {end} is {total}')
#-------------------✅---------------------------


"""---------------🚨`examples 3`---------------------"""
even_nums = []

for num in range(2, 21, 2):
	even_nums.append(num)
print(even_nums)


items_in_database = 10

for num in range(items_in_database, 0, -1):
	print("Items remaining:", num)
    # Perform the sale operation or any other desired operation here
    # You can decrement the value of items_in_database or update your database accordingly
#-------------------✅---------------------------


print(result)
print(students_names)


for key, value in students_names.items():
    print(key, ":", value)


for index, (name, age) in enumerate(students_names.items()):
    print(f'Students {index+1}: {name} - {age} years old')


students_dic = {'name': 'tech', 'age': 22}


for index, row in enumerate(students_dic):
	print(index, row)


"""---------------🚨`examples 4 length`---------------------"""
my_string = "Hello, World!"
string_length = len(my_string)
print(string_length)  # Output: 13

my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print(list_length)  # Output: 5

my_dict = {"name": "John", "age": 30}
dict_length = len(my_dict)
print(dict_length)  # Output: 2

my_range = range(1, 10)
range_length = len(my_range)
print(range_length)  # Output: 9
#-------------------✅----------------------------------------


"""---------------🚨`examples 4 white space`---------------------"""
x = 10

if x > 0:
    print("Positive number")
    if x % 2 == 0:
        print("Even number")
else:
    print("Negative number")


my_string = "Hello    World"

# Replace any whitespace in "my_string" with a hyphen ("-") and print the modified string.
modified_string = my_string.replace(" ", "-")
print(modified_string)

#-------------------✅----------------------------------------



"""---------------🚨`examples 4 split`---------------------"""
my_string = "Hello,World"
split_result = my_string.split(",")
print(split_result)  # Output: ['Hello', 'World']

sentence = "Python is a popular programming language"
word_list = sentence.split()
print(word_list)  # Output: ['Python', 'is', 'a', 'popular', 'programming', 'language']

numbers = "1-2-3-4-5"
number_list = numbers.split("-")
print(number_list)  # Output: ['1', '2', '3', '4', '5']
