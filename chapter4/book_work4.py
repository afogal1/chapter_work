# using range() function 
for value in range(1,5):
    print(value)

# using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

# square numbers list
squares = []    # start with an empty list called squares 
for value in range(1,11):   # tell Python to loop through each value from 1 to 10 using the range() function
    square = value**2   # current value is raised to the second power 
    squares.append(square) # each new value of square is appended to the list squares 
print(squares)

# to condense the code, try this:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# simple statistics with a list of numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions, condenses the list even more from line 16:
squares = [value**2 for value in range(1,11)]
print(squares)

# make a list of odd numbers from 1 to 20:
odd_numbers = list(range(1,20,2))
print(odd_numbers)

# make a list of the multiples of 3 from 3 to 30:
multiple = list(range(3,30,3))
print(multiple)

# make a list of the first 10 cubes from 1 - 10:
cube = list(range(1,10,2**3))
print(cube)

# use a list comprehension to generate a list of the first 10 cubes:
cubes = [2**3 for value in range(1,11)]
print(cubes)

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#looping through a slice
players = ['charles', 'martina', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copying a list 
my_foods = ['pizza', 'falafel', 'carrot cake']  #make a list of foods
friend_foods = my_foods[:]  # make a new list and make a copy of my_foods by asking for a slice of my_foods
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# add new food to each list 
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]  
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nThe first three items in the list are")
print(players[:-2])
print("\nThree items from the middle of the list are")
print(players[1:4])
print("\nThe last three items in the list are\n")
print(players[1:]) 

#example
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_pizza = my_foods[:]
my_foods.append("bacon")
friend_pizza.append("tacos")
print("my favorite pizzas are:")
print(my_foods)
print("\n My favorite pizzas are:")
print(my_foods)

#Tuple example:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# if you try to change one of the items in the tuple it will come up as an error 
#dimensions[0] = 250

#looping through all values in a tuple:
#designs = (200, 50)
#for design in designs:
    #print(design)

# writing over a tuple
dimensions = (200, 50)      # defines original tuple 
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)     # store a new tuple in the variable dimensions 
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#another tuple example
simple_foods = ('pizza', 'cake', 'burgers', 'tacos', 'eggs')
print("\nRegular Menu:")
for simple_food in simple_foods:
    print(simple_food)
simple_foods = ('pizza', 'cake', 'burgers', 'milk', 'toast')
print("\nUpdated Menu:")
for simple_food in simple_foods:
    print(simple_food)

