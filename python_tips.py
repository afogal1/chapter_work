#1 Forgetting to Indent
# always indent the line after the for statement in a loop. If you forget, Python will remind you:
# Example:

#magicans = ['alice', 'david', 'carolina']
#for magician in magicans:
#print(magician)

# will come up as an error because you forgot to indent after the statement in a loop 

#2 Indenting unnecessarily after the loop
# if you indent code that should run after a loop, the code will be repeated 
#example

magicans = ['alice', 'david', 'carolina']
for magician in magicans:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print("Thank you everyone, that was a great magic show!")

# Since line 19 was indented, it will be about of the loop

#3 Forgetting the colon 
# the colon at the end of a for statement tells Python to interpret the next line as the start of a loop
#example:

magicans = ['alice', 'david', 'carolina']
for magician in magicans: #: don't forget the colon 
    print(magician)

# del - removes an item from the list
# pop() - removes the last item in a list, but lets you work with it after removing it

# SLICE - a specific group of items in a list 

# TUPLE - immutable list - refers to values that cannot change as immutable 
# Tuple also uses () instead of []

# styling your code:
# when someone wants to make a change to the Python language, they write a Python Enhancement Proposal (PEP):
# PEP 8 recommends that you use four spaces per indentation level

# F"" means formatted string 

# Conditional Test - if statement is an expression that can be evaluated as True or False

# (!=) - not equal

# A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated

# A dictionary in Python is a collection of key-value pairs. 
# Each key is connected to a value, and you can use a key to access the value associated with that key.

# A set is similar to a list except that each item in the set must be unique

# Keys are the first part in a dictionary 
# Values are the second part in a dictionary 

# Nesting - storing a set of dictionaries in a list or a list of items as a value in a dictionary

# "\t" to indent 

# break statement will exit a while loop immediately without running any code 