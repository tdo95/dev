import math

name = 'Tee'
items = [1,2,3,4,5,6]
#multiline template string
multiline = f'''Yes, Im {name}, a multiline string How do you do?'''
#length of string
len(name)
#Capitalize first letter of each word
multiline.title()
#Replace matching values in string
name.replace('e', 'E')
#Copy array
items[:]
#Copy part of array
items[:2] #mising 1st param assumed zero
items[0:] #mising 2nd param assumed end of array
items[0:-2] #negative varaibles start from the end
print(items[-2:-4])

# operations
num = 10 // 3 #returns integer
expo = 10 ** 2 #returns 10 to the power of 3

# order of operations
# parenthesis
# exponentiation
# multiplication or division
# addition or subtraction

# math functions
abs(num) #absolute value
round(num)
math.ceil(num)
print(math.floor(2.9))

# if statement
is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
    
house_price = 1000000
good_credit = True
if good_credit: 
    print(f'Put down 10%, ${house_price * .1}')
    
else:
    print(f'Put down 20%, ${house_price * .2}')

# Logical operators
# and
# or
# not

high_income = True
good_cred = True

if high_income and not good_cred:
    print('eligable for loan')


# comparison operator
# >
# >=
# <
# <=
# ==
# !=

username = 'Tee'

if len(username) < 3:
    print('name must be at least 3 character')
elif len(username) > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good')

# weight = input('Weight: ')
# weight_type = input('(L)bs or (K)g?: ')

# if weight_type.lower() == 'k':
#     print(f'Your weight is {float(weight) * 0.45} Kilos')
# elif weight_type.lower() == 'l':
#     print(f'Your weight is {float(weight) / 0.45} Pounds')
# else:
#     print('Please enter a valid option')

# while loop

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print('Done')

# secret_num = 3
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_num:
#         print('You won')
#         break
# else:
#     print('Sorry you failed!')

# is_typing = True
# old_input = ""
# while is_typing:
#     user_input = input('>').lower()
#     if user_input == old_input:
#         print(f'Car is already in {user_input}')
#     elif user_input == 'start':
#         print('Car started...Ready to go!')
#     elif user_input == 'stop':
#         print('Car stopped.')
#     elif user_input == 'quit':
#         is_typing = False
#     else:
#         print('I dont understand that...')
#     old_input = user_input

# for loop

# prices = [10,20,400,20,10]
# sum = 0
# for item in prices:
#     sum += item
# print(sum)

# numbers = [2,2,2,5,5]

# for length in numbers:
#     line_value = ''
#     for num in range(length):
#         line_value += 'x'
#     print(line_value)

# LISTS

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Sniper'
# print(names[0:4])

nums = [2323,12312123,2332,2,3,232,43,23]

largest = nums[0]
for number in nums:
    if number > largest:
        largest = number
print(largest)

# 2D Lists
matrix = [
[1,2,3],
[4,4,5],
[3,3,4]
]
# Modify items dirctly
matrix[0][1] = 20

# List Methods

numbers = [2,3,4] 
# appends to the end of a list
numbers.append(39)
# inserts value at index
numbers.insert(0, 10)
# finds value and removes it
numbers.remove(2) # returns error if item not in list
# check existance of an item
numbers.index(4) # returns an error if value doesnt exit
# clears all values inlist
numbers.clear()
4 in numbers # returns true or false, safer to use
# count amount of items
numbers.count(3)
# sort list in place
numbers.sort()
# reverse order of list
numbers.reverse()
# copy list
numbers2 = numbers.copy()

# tuple
numbers = (1,2,3)
# count occurences of an item
numbers.count(3)
# find index whre an item exists
numbers.index(2)


# unpacking - similar to destructuring in js

# works with lists and tuples
coordinate = (1,2,40)
x, y, z = coordinate

# dictionaires

customer = {
    "name": 'jon',
    "age": 40,
    "is_verified": True
}
customer["name"] #returns an error if key doesnt exist
customer.get("birthdate", "Jan 3") # no error if key doesnt exist, can supply default value

numberMap = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
    '0':'Zero'
}
# num = input('Number: ')
# num_str = ''
# for digit in num:
#     num_str += f'{numberMap.get(digit,"#")} '
# print(num_str)

# FUNCTIONS

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')

def say_hello(name):
    print('Hi there')
    print(f'Nice to meet you {name}')
# keyword arguemnts (no reliance on postion)
# positional arguemnts should always come first
greet_user(name='Tee')

# None represents the  absence of a value (like null)


# exceptions - how to handle errors in python
# try:
#     age = int(input('Age: '))
#     print(age)
#     income = 1000 / age
# except ValueError:
#     print('Invalid value')
# except ZeroDivisionError:
#     print('Age can not be 0')


# classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10,2)
point1.draw()
point1.x = 1


class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'Hello, My name is {self.name}')

tee = Person('Tee')
tee.talk()

class Teacher(Person):
    def __init__(self, name, class_size):
        super().__init__(name)
        self.class_size = class_size
    pass # Tells python to pass this line 

trey = Teacher('Trey', 30)

trey.talk()
print(trey.class_size)