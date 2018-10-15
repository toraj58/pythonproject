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