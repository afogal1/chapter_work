# a simple dictionary 
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!")

# adding new key value pairs 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#  starting with an empty dictionary 
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary 
alien_0 = {'color': 'green'}
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# example: track the position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
#  Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3
# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))

# Removing key value pairs 
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)

del alien_1['points']
print(alien_1)

# a dictionary of similar objects 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("\nSarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# try it yourself 
friend = {'first_name': 'brad', 'last_name': 'willet', 'age': 26, 'city': 'bloomington'}
print("\nMy friend is " + friend['first_name'].title() +
    "." + " His last name is " + friend['last_name'].title() +
    "." + " Brad is " + str(friend['age']) + " years old." +
    " He grew up in " + friend['city'].title() + " Illinois.")

# try is yourself 
favorite_numbers = {
    'mike': 7,
    'bob':  8,
    'jill': 9,
    'larry': 10,
    'brandon': 11
}
print("\nBobs favorite number is " +
    str(favorite_numbers['bob']) + ".")

# looping through a dictionary 
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items(): # create names for the variables like key and value 
    print("\nKey: " + key)
    print("Value: " + value)

# another looping example 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "' favorite language is " +
    language.title() + ".")

# looping through all the key in a dictionary 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# another looping example
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
    ", I see your favorite language is " +
    favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

# looping through a dictionary's keys in order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
if 'alex' not in favorite_languages.keys():
    print("Alex, please take the poll!")

# looping through all values in a dictionary 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# using a set (won't repeat any values)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("\nThe folowing languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# try it yourself
major_rivers = {
    'nile': 'egypt',
    'Mekong': 'asia',
    'Indus': 'karachi',
}
for river, country in major_rivers.items():
    print(" The " + river.title() + " runs through " +
    country.title())

# try it yourself 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title() + "\nThank you for taking the poll!")
if 'alex' not in favorite_languages.keys():
    print("Alex, please take the poll")

# nesting a list of dictionaries 
alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]    # pack each dictionary into a list 

for alien in aliens:
    print(alien)

# create a fleet of 30 aliens 
# first make an empty list for storing aliens
aliens = []

for alien_number in range(30):  #returns a set of numbers which tells python how many times the loop will repeat
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}    #each time loop runs we create a new alien
    aliens.append(new_alien)
# next show the first 5 aliens 
for alien in aliens[:5]:    # use a slice to print the first five aliens
    print(alien)
print("...")
# next show how many aliens have been created 
print("Total number of aliens: " + str(len(aliens)))    #print the length of the list (30)


# change aliens on the list above
aliens = []

for alien_number in range(0,30):  
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}    
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    
for alien in aliens[0:5]:   
    print(alien)
print("...")


# a list in a dictionary 
# store information about a pizza being ordered 
pizza = {
    'crust': 'thick',
    'toppings': ['mushroooms', 'extra cheese'],
}
# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# another example 
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# a dictionary in a dictionary 
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

