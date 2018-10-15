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
