# the while loop
# while Boolean or Bollean expression:
    # code block
    # condition is true 


# You must be over 5 feet to ride my ride
# I have a magic potion that will let you grow one inch everytime you use it!
height = 55 
while height < 60:
    print(f"You are {height} inches tall \n and too short to ride!")
    print("Drink my magic potion")
    height += 1

print("Thanks for coming")

# input function
height1 = int(input("What is your height in inches? "))
while height1 < 60:
    print(f"You are {height1} inches tall \n and too short to ride!")
    print("Drink my magic potion")
    if height1 == 58:
        break
    height1 += 1

print("Thanks for coming")


# another example 
while True:
    response = input("What do you want to do? Say hi [h], say goodbye [g], or quit?[q] ")
    if response.lower() == "h":
        print("hello)")
    elif response.lower() == "g":
        print("goodbye")
    elif response.lower() == "q":
        break
    else:
        print("invalid option")

