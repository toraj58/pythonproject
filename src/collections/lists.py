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

# List objects also have useful methods which we can call:

print('-----------------------------------------------')

numbers = [1, 2, 3, 4, 5]

# we already saw how to add an element to the end
numbers.append(5)

# count how many times a value appears in the list
numbers.count(5)

# append several values at once to the end
numbers.extend([56, 2, 12])

# find the index of a value
numbers.index(3)
# if the value appears more than once, we will get the index of the first one
numbers.index(2)
# if the value is not in the list, we will get a ValueError!
# numbers.index(42)

# insert a value at a particular index
numbers.insert(0, 45) # insert 45 at the beginning of the list

# remove an element by its index and assign it to a variable
my_number = numbers.pop(0)

# remove an element by its value
numbers.remove(12)
# if the value appears more than once, only the first one will be removed
numbers.remove(5)

# [Touraj] :: good to know following information:

# Python has a built-in array type. It’s not quite as restricting as an array in C or Java
#  – you have to specify a type for the contents of the array, and you can only use it to store numeric
# values, but you can resize it dynamically, like a list. You will probably never need to use it.