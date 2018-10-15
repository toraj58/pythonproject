from builtins import print

# Python has another sequence type which is called tuple.
# Tuples are similar to lists in many ways, but they are immutable.
# We define a tuple literal by putting a comma-separated list of values inside round brackets (( and )):

# What are tuples good for? We can use them to create a sequence of values that we don’t want to modify.
#  For example, the list of weekday names is never going to change. If we store it in a tuple,
#  we can make sure it is never modified accidentally in an unexpected place:

print('--------------------------Tuples-----------------------------')

animals = ('cat', 'dog', 'fish')

# an empty tuple
my_tuple = ()

# we can access a single element
print(animals[0])

# we can get a slice
print(animals[1:]) # note that our slice will be a new tuple, not a list

# we can count values or look up an index
animals.count('cat')
animals.index('cat')

# ... but this is not allowed:
# animals.append('canary')
# animals[1] = 'gerbil'

# Here's what can happen if we put our weekdays in a mutable list

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def print_funny_weekday_list(weekdays):
    weekdays[5] = 'Caturday' # this is going to modify the original list!
    print(weekdays)

print_funny_weekday_list(WEEKDAYS)

print(WEEKDAYS) # oops

# Also in the formatting string in print we actually using tuples!
print("%d %d %d" % (1, 2, 3))

print('-------------------------------Sets-----------------------------------')

animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
print(animals) # the set will only contain one cat

even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

# numbers which are big or even but not both
print(big_numbers ^ even_numbers)

# It is important to note that unlike lists and tuples sets are not ordered.
# When we print a set, the order of the elements will be random.
# If we want to process the contents of a set in a particular order,
# we will first need to convert it to a list or tuple and sort it:

# Printing unsorted set
print(animals)

# Printing set after sorting
# The sorted function returns a list object.
print(sorted(animals))

# [Touraj] : Important to know:
# this is an empty dictionary
a = {}

# this is how we make an empty set
b = set()

print('---------------------------------Ranges-----------------------------------')

# range is another kind of immutable sequence type. It is very specialised
# – we use it to create ranges of integers. Ranges are also generators.
# We will find out more about generators in the next chapter, but for now
# we just need to know that the numbers in the range are generated one at
# a time as they are needed, and not all at once. In the examples below,
# we convert each range to a list so that all the numbers are generated and we can print them out:

# print the integers from 0 to 9
print(list(range(10)))

# print the integers from 1 to 10
print(list(range(1, 11)))

# print the odd integers from 1 to 10
print(list(range(1, 11, 2)))


print('-------------------------------Dictionaries--------------------------------')

# Like sets, dictionaries are not ordered – if we print a dictionary, the order will be random.

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

personal_details = {
    "name": "Jane Doe",
    "age": 38, # trailing comma is legal
}

print(marbles["green"])
print(personal_details["name"])

# This will give us an error (KeyError), because there is no such key in the dictionary
# print(marbles["blue"])

# modify a value
marbles["red"] += 3
personal_details["name"] = "Jane Q. Doe"

print(marbles["red"])
print(personal_details["name"])

battleship_guesses = {
    (3, 4): False,
    (2, 6): True,
    (2, 5): True,
}

surnames = {} # this is an empty dictionary
surnames["John"] = "Smith"
surnames["John"] = "Doe"
print(surnames) # we overwrote the older surname

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
marbles["blue"] = 30 # this will work
# marbles["purple"] += 2 # this will fail(KeyError) -- the increment operator needs an existing value to modify!

# [Touraj] : commonly used methods of dictionary objects:

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

# Get a value by its key, or None if it doesn't exist
marbles.get("orange")
# We can specify a different default
marbles.get("orange", 0)

# Add several items to the dictionary at once
marbles.update({"orange": 34, "blue": 23, "purple": 36})

# All the keys in the dictionary
print(marbles.keys())
# All the values in the dictionary
marbles.values()
# All the items in the dictionary
marbles.items()

# [Touraj] check if key exists in a dictionary using in or not in
print("purple" in marbles)
print("white" not in marbles)

# [Touraj] :: check if a value exists in a dictionary
print("Smith" in surnames.values())
print("Doe" in surnames.values())





