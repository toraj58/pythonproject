# a list of strings
from builtins import print

animals = ['cat', 'dog', 'fish', 'bison']

# a list of integers
numbers = [1, 7, 34, 20, 12]

# an empty list
my_list = []

one_variable = 'touraj'
another_variable = 'vitalii'
third_variable = 'daniel'

# a list of variables we defined somewhere else
things = [
    one_variable,
    another_variable,
    third_variable, # this trailing comma is legal in Python
]

print(animals[0]) # cat
print(numbers[1]) # 7

# This will give us an error, because the list only has four elements
# print(animals[6])

print(animals[-1]) # the last element -- bison
print(numbers[-2]) # the second-last element -- 20

#  Extracting a subset of the list
print(animals[1:3]) # ['dog', 'fish']
print(animals[1:-1]) # ['dog', 'fish']

print('----------------------------')

print(animals[2:]) # ['fish', 'bison']
print(animals[:2]) # ['cat', 'dog']
print(animals[:]) # a copy of the whole list

# We can even include a third parameter to specify the step size:
print(animals[::2]) # ['cat', 'fish']


# Lists are mutable
# – we can modify elements, add elements to them or remove elements
# from them. A list will change size dynamically when we add or remove elements
# – we don’t have to manage this ourselves:

# assign a new value to an existing element
animals[3] = "hamster"

# add a new element to the end of the list
animals.append("squirrel")

# remove an element by its index
del animals[2]

print('----------------------------')

# Because lists are mutable, we can modify a list variable without assigning the variable
#  a completely new value. Remember that if we assign the same list value to two variables,
#  any in-place changes that we make while referring to the list by one variable name will
#  also be reflected when we access the list through the other variable name:

animals = ['cat', 'dog', 'goldfish', 'canary']
pets = animals # now both variables refer to the same list object

animals.append('aardvark')
print(pets) # pets is still the same list as animals

animals = ['rat', 'gerbil', 'hamster'] # now we assign a new list value to animals
print(pets) # pets still refers to the old list

pets = animals[:] # assign a *copy* of animals to pets
animals.append('aardvark')
print(pets) # pets remains unchanged, because it refers to a copy, not the original list

# We can mix the types of values that we store in a list:
my_list = ['cat', 12, 35.8]

numbers = [34, 67, 12, 29]
my_number = 67


# How do we check whether a list contains a particular value? We use in or not in, the membership operators:

numbers = [34, 67, 12, 29]
number = 67

if number in numbers:
    print("%d is in the list!" % number)

my_number = 90
if my_number not in numbers:
    print("%d is not in the list!" % my_number)

print('-----------------------------------------------')

# There are many built-in functions which we can use on lists and other sequences:

# the length of a list
print(len(animals))

# the sum of a list of numbers
print(sum(numbers))

# are any of these values true?
print(any([1,0,1,0,1]))

# are all of these values true?
print(all([1,0,1,0,1]))
