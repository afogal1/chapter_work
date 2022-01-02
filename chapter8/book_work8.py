# defing a function
def greet_user():   # defining a function 
    """Display a simple greeting.""" # docstring: which describes what the function does (""" """)
    print("\nHello!") # function call: tells python to execute the code in the function 

greet_user()


# passing information to a function 
def greet_user1(username):
    """Display a simple greeting."""
    print("\nHello, " + username.title() + "!")

greet_user1('jesse')


# try it yourself 
def display_message():
    """Display what we will be learning."""
    print("\nWe will be learning about functions.")

display_message()


# try it yourself 
def favorite_book(title):
    """"Display our favorite books."""
    print("\nOne of my favorite books is " + title.title() + "!")

favorite_book('Alice in Wonderland')


# positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') 
# argument hamster is stored in the parameter animal_type
# argument harry is stored in the parmeter pet_name


# multiple function calls 
def describe_pet1(animal_type1, pet_name1):
    """Display information about a pet."""
    print("\nI have a " + animal_type1 + ".")
    print("My " + animal_type1 + "'s name is " + pet_name1.title() + ".")

describe_pet1('hamster', 'harry')
describe_pet1('dog', 'willie')


# keyword arguments: 
# A keyword argument is a name-value pair that you pass to a function
def describe_pet2(animal_type2, pet_name2):
    """Display information about a pet."""
    print("\nI have a " + animal_type2 + ".")
    print("My " + animal_type2 + "'s name is " + pet_name2.title() + ".")

describe_pet2(animal_type2 = 'hamster', pet_name2 = 'harry')


# Default Values:
# when writing a function, you can define a default value for each parameter
def describe_pet3(pet_name3, animal_type3='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type3 + ".")
    print("My " + animal_type3 + "'s name is " + pet_name3.title() + ".")

describe_pet3('willie')


# try it yourself 
def make_shirt(size, text):
    """Display shirt size and shirt text."""
    print("\nThe shirt size is " + size.title() + "." )
    print("\nThe shirt text is " + text.title() + "." )

make_shirt('medium', 'bold')    # positional argument
make_shirt(size='medium', text='bold')  # keyword arguments


#try it yourself
def make_shirt2(size2='large', text2='medium'):
    """Display shirt size and shirt text."""
    print("\nThe shirt size is " + size2.title() + "." )
    print("\nThe shirt text is " + text2.title() + "." )

make_shirt2()


# try it yourself 
def describe_city(city, country='usa'):
    """Display cities in a country"""
    print(city.title() + "is in the " + country.title() + ".")

describe_city('chicago')
describe_city('boston')
describe_city('washington')


# return values
# The return statement takes a value from inside a function and sends it back to the line that called the function
# returning a simple value 
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name # the value of the full_name is converted to title case 
    return full_name.title()                 # then returned to the calling line 

musician = get_formatted_name('jimi', 'hendrix')    # return value is restored in the variable(musician)
print(musician)


# making an argument optional 
def get_formatted_name1(first_name1, middle_name1, last_name1):
    """Return a full name, neatly formatted."""
    full_name1 = first_name1 + ' ' + middle_name1 + ' ' + last_name1
    return full_name1.title()

musician1 = get_formatted_name1('john', 'lee', 'hooker')
print(musician1)


# another example
def get_formatted_name2(first_name2, last_name2, middle_name2=''): # the middle name is optional so it's listed last
    """Return a full name, neatly formatted."""
    if middle_name2:
        full_name2 = first_name2 + ' ' + middle_name2 + ' ' + last_name2 #empty strings '' are always true
    else:
        full_name2 = first_name2 + ' ' + last_name2
    return full_name2.title()

musician2 = get_formatted_name2('jimi', 'hendrix')
print(musician2)

musician2 = get_formatted_name2('john', 'hooker', 'lee')
print(musician2)


# returning a dictionary 
def build_person(first_name3, last_name3):
    """Return a dictionary of information about a person."""
    person = {'first': first_name3, 'last': last_name3}
    return person

musician3 = build_person('jimi', 'hendrix')
print(musician3)


# same example above just with age added
def build_person1(first_name4, last_name4, age=''):
    """Return a dictionary of information about a person."""
    person1 = {'first': first_name4, 'last': last_name4}
    if age:
        person1['age'] = age
    return person1

musician4 = build_person1('jimi', 'hendrix', age=27)
print(musician4)


# using a function with a while loop
