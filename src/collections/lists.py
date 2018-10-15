# a list of strings
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

