# if statements 
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'     # sets the value of car to 'bmw'
car == 'bmw'    # checks whether the value of car is 'bmw' 
# true

# checking for equality 
car = 'audi'
car == 'bmw'
# false 

car = 'Audi'
car.lower() == 'audi'
# true 

# checking for inequality 
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':    # compares the value of requested_topping to the value of anchovies 
    print("\nHold the anchovies!")

# Numerical Comparisons 
answer = 17 
if answer != 42:
    print("\nthat is not the correct answer. Please try again!\n")

# checking multiple conditions using and
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# false 
age_1 = 22
age_0 >= 21 and age_1 >= 21
# true 

# checking multiple conditions using or 
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
# true 
age_0 = 18
age_0 >= 21 or age_1 >= 21
# false 

# checking whether a value is in a list 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
# true 
'pepperoni' in requested_toppings
# false 

# checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.\n") 

# Boolean expressions 
game_active = True 
can_edit = False 

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

bird = 'crow'
print("\nis bird == 'crow'? I predict true.")
print(bird == 'crow')
print(bird != 'eagle')
print("\nis bird == 'pelican'? I predict false.")
print(bird == 'pelican')

car = 'Audi'
car.lower() == 'audi'
print(car.lower() == 'audi')

answer = 20
if answer != 40:
    print("\nis not correct")

age_0 = 19
age_1 = 18
if age_0 or age_1 >= 21:
    print("not correct")

# if-else statements 
age = 20
if age >= 18:
    print("\nyou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nYou are not old enough to vote!")
    print("Please register to vote as soon as you turn 18!")

# the if-elif-else chain
age = 12 
if age < 4:
    print("\nYour admission cost is $0.")
elif age <18:
    print("\nYour admission cost is $5.")
else:
    print("\nYour admission cost is $10.")

# condense version from above 
age = 12 
if age < 4:
    price = 0 
elif age < 18:
    price = 5 
else:
    price = 10
print("\nYour admission cost is $" + str(price) + ".")

# using multiple elif blocks 
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10 
else:
    price = 5
print("\n Your admission cost is $" + str(price) + ".")

# omitting the else block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10 
elif age >= 65:
    price = 5
print("\n Your admission cost is $" + str(price) + ".")

# testing multiple conditions 
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

alien_colors = ['green', 'yellow', 'red']
for alien_color in alien_colors:
    if alien_color == 'green':
        print("\nplayer just earned 5 points.")
    elif alien_color == 'yellow':
        print("\nplayer just earned 10 points.")
    else:
        print("\nplayer just earned 15 points.")

variable_age = 70 
if variable_age < 2:
    print("\nThat person is a baby.")
elif variable_age < 4:
    print("\nThat person is a toddler.")
elif variable_age < 13:
    print("\nThat person is a kid.")
elif variable_age < 20:
    print("\nThat person is a teenager.")
elif variable_age < 65:
    print("\nThat person is an adult.")
else:
    print("\nThat the person is an elder.")


favorite_fruits = ['apple', 'orange', 'blueberry']
if 'peach' in favorite_fruits:
    print("I like peaches.")
if 'apple' in favorite_fruits:
    print("I like apples.")
if 'strawberry' in favorite_fruits:
    print("I like strawberries")
if 'orange' in favorite_fruits:
    print("I like oranges.")
if 'blueberry' in favorite_fruits:
    print("I like blueberries.")

# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("\nAdding" + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':        # checks to see if person requested green peppers
        print("\nSorry, we are out of green peppers right now.")
    else:
        print("\nAdding " + requested_topping + ".")
print("\nFinished making your pizza!")

# checking that a list is not empty 
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings: # a quick check for the toppings
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?") # since there are no toppings, the list comes back as false

# using multiple lists 
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:    # loop through list of requested toppings 
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".")
    else:
        print("\nSorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# example 
usernames = ['admin', 'jim1', 'bob2', 'erin4', 'lucy5']
for username in usernames:
    if 'admin' in username:
        print("\nhello admin, would you like to see a status report?\n") 
    else:
        print("Hello " + username.title() +", " + "thank you for logging in again.")
if usernames : []
print("We need to find some users!")

# example 
current_users = ['bob', 'alex', 'larry', 'jimmy', 'mark']
new_users = ['bob', 'alex', 'brian', 'justin', 'mike']
for new_user in new_users:
    if new_user in current_users:
        print(new_user.title() + " Will have to use a new username\n.")
    else:
        print(new_user.title() + " that username is available.\n")

# hi 
