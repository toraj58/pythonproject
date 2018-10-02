import sys
import random
import os
import time
import calendar
import math
from builtins import print
import support

def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


def myfunc():
    print('\n\nstarting new python Function\n\n')
    return

def printme2( str ):
   "This prints a passed string into this function2"
   print(str)
   return;


myfunc()

support.printsupport('df')
support.printsupport2("dsfgnh9")

support.printsupport3('Finally Modules Recognized')

print("Hello, Python!")
print("Hello, Python!")
print("Hello, Python!")

path = os.environ['PATH']
user = os.environ['USER']
# abc = os.environ['ABC_VAR']
print(path)
print("user ::", user)
# print("ABC_VAR ::", abc)

counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string

a = b = c = 1

a, b, c = 1, 2, "john"

if True:
    print("Py True")
else:
    print("Py False")

total = "item_one" + \
        "item_two" + \
        "item_three"

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

flag = "false"

if flag == "false":
    print("done")

print(days)
print(total)

x = 'fooo'
sys.stdout.write(x + '\n')

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(tinylist)
print("---------")

sys.stdout.write('Python Select Random form List\n')

print(random.choice(list))
print(random.choice(tinylist))

# Tuples are like list but can not be changed
# They Are like readonly list
tuple = ('abcd', 786, 2.23, 'john', 170.2)
tinytuple = (123, 'john')

print(tuple)

# Python Dictionary

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict)
print(tinydict)
print(2 ** 4)

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

flager1 = None
flager2 = False
flager3 = True

print('<><><><><><><><><><><><><><>')

if flager3:
    print("pig")

printme("voohey")

var1 = 'abcdefgh'
print(var1[:3])
print(var1[1:3])
print(var1[2:6])
print(var1[3:3])  # should write empty to console

print(str.upper(r'C:\\nowhere'))  # Printing Raw String ...

title = str.center('DEMO', 100, '-')
title2 = str.center('MMT BLOOM DEMO', 100, '-')
print(title)
print(title2)

# How to Delete ITEM in Python List::

list1 = ['physics', 'chemistry', 1997, 2000];
print(list1)
del list1[2];
print("After deleting value at index 2 : ")
print(list1)
print(len(list1))  # Printing Length of the List

tup = ('physics', 'chemistry', 1997, 2000);
print(tup);
del tup;  # you can Only Remove whole Tuple, It is not Necessary to delete individual tuples from Tuples because Tuples are Immutables.
print("After deleting tup : ")
# print(tup)

i = 1
for x in (1, 2, 3, 'jij', 'ik'):
    i += 1
    print(x)
    print('next')
    print('i :: ', i)


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

# Important notes about Python Dictionary Keys:

# (a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example −

# (b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example −


localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

cal = calendar.month(2008, 1)
print("Here is the calendar:\n\n")
print(cal)

print("python Callendar :: ")
print("\n\n")

days = ['f1', 'f2', 'f3']
days[2] = 'fff'
print(days)
print(days[:2])
print(days[1:2])

printme2(str = 'hey')

# Python Lambda Functions (anonymous functions) :

van = sum = lambda arg1, arg2: arg1 + arg2;

print(sum(100,200))
print(van(100,200))


# Dir Function list the names of all the modules, variables and functions that are defined in a module. Following is a simple example:
prnmathdir = dir(math)
print(prnmathdir)

# Printing Python Current Directory...
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#Python Smart List Generate ::
#The following command will generate a list in the spefied range also multiply each item with 5
smartList = [x*5 for x in range(2,10,2)]

for x in smartList:
    print('Smart List Item :: ', x)


# following try to create a new directory in the current path
# if directory exists then it throw and exception complaining that dir already exists.
# os.mkdir("zeedir")

# The Following command (getcwd) get the current working directory
# Also you can use chdir command to change the current direcitry.
# For removing a directory just use : rmdir
currentPath = os.getcwd()
print("Current Directory is :: ", currentPath)
# os.rmdir("zeedir")


# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite
