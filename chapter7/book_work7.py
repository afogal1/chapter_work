#  writing clear prompts 
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")


# Using int() to accept numerical input 
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# the modulo operator 
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nthe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


# try it yourself
rental_car = input("What kind of rental car would you like?: ")
if rental_car == "Subaru":
    print("Let me see if I can find you a Subaru")
else:
    print("I'm sorry, we do not have that vehicle.")


# while loops 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# using break to exit a loop 
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:     # a loop will run forever unless it reaches a break statement 
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# using a continue in a loop
# consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:
current_number1 = 0
while current_number1 < 10:
    current_number1 += 1    # count by 1 
    if current_number1 % 2 == 0: # current number is divisible by 2 
        continue

    print(current_number1)


# avoiding infinite loops
x = 1 
while x <= 5:
    print(x)
    x += 1 #if you omit this line, the loop will run forever, printing a series of 1's 


# try it yourself
prompt1 = "\nYou'll add that topping to their pizza."
prompt1 += ("\nEnter 'quit' when your are finished ")

while True:
    pizza_toppings = input(prompt1)

    if pizza_toppings == 'quit':
        break
    else:
        print("Great choice")

# try it yourself
age = int(input("\nWhat is your age?"))

if age < 3:
        print("The ticket is free.")
elif age < 12:
        print("The ticket is $10.")
else:
        print("The ticket is $15.")    


#  using a while loop lists and dictionaries 
# moving items from one list to another:

# start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()    # removes unverified users one at a time d

    print("Verifying user: " + confirmed_user.title())
    confirmed_users.append(confirmed_user)

#  Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# removing all instances of specific values from a list 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


# filling a dictionary with user input 
responses = {}
#  set a flag to indicate that polling is active 
polling_active = True 

while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?" )

    # store the response in the dictionary 
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False 

# polling is complete. show the results 
print("/n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


# try it yourself 
sandwich_orders = ['bacon', 'tuna', 'cheese', 'ham']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_orders)
    print("I made your" + sandwich_orders.title())
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwiches)








