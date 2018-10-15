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
