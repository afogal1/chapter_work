# Boolean can be two things: ON or OFF, True or False, Yes or No
my_bool = True
print(my_bool)
my_bool = False 
print(my_bool)
print(bool(0)) # boolean of 0 is always false 

print(bool())       # empty list is false 
print(bool('word')) # string inside is true 

# boolean expressions:
# > < >= <= == !=
print("dog" == "cat")
print("dog" == "dog")
print(4 < 6)

x = 10 
print(5 < x < 20)

letter = "a"
print(letter > "b")

# 2 conditions 
x = 10
y = 10
z = 20

print(x == 10 and y == 10)
print( x == y)

x = 8
x = 9
print(not x != y)
print(not True or False)

# if statement 
# if BOOLEAN OR BOOLEAN EXP:
    # code block
    # for if true 
# else:
    # for the if false code block 

height = 55

# must be 5 feet tall to ride my ride 
# must be under 6 feet tall to ride 

if height < 55:
    print("You are too short")
    print("I am sorry but get oof of my ride!")
elif height > 72:
    print("You are too tall!")
    print("Get of my ride!")
else:
    print("Enjoy the Ride!")
print("Thanks for visiting!")
