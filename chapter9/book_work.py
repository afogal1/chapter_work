# Object-oriented programming is one of the most effective approaches to writing soft-ware
# 1) dog.py example 
class Dog():
    
    def __init__( self, name, age):   #self,name,age are parameters  # a function that is part of a class is a method 
        # name and age attributes
        self.name = name
        self.age = age 

    def sit(self):
        #  simulate a dog sitting in response to a command
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # simulate rolling over in response to a command
        print(self.name.title() + " rolled over!")

# Making an Instance from a Class
my_dog = Dog('willie', 6) #arguments store in variable my_dog
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old. ")
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.") 

# Calling Methods 
my_dog.sit()
my_dog.roll_over()
your_dog.sit()


# Try it yourself
class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type 

    def describe_restaurant(self):
        print(f'{self.name} is beautiful and is a {self.type} of place.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')

place = Restaurant('Popbelly', 'Mexican')
spot = Restaurant('Crabs', 'Seafood')
hangout = Restaurant('Papa Johns', 'American')

place.describe_restaurant()
place.open_restaurant()
spot.describe_restaurant()
hangout.describe_restaurant()

# try it yourself 
class User():

    def __init__(self, firstName, lastName, picture):
        self.firstName = firstName
        self.lastName = lastName 
        self.picture = picture

    def describeUser(self):
        print(f'{self.firstName} {self.lastName} is {self.picture}')

    def greetUser(self):
        print(f'Hello {self.firstName} {self.lastName} how are you today!?')

westCoast = User('Bob', 'Larry', 'tall')
eastCoast = User('Mackenzie', 'Farmer', 'short')

westCoast.describeUser()
westCoast.greetUser()
eastCoast.describeUser()
eastCoast.greetUser()


# working with Classes and Instances
# 2) car.py
"""A class that can be used to represent a car.""" # use a docstring that briefly describes the contents of this module.
class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model 
        self.year = year 
        self.odometerReading = 0   # setting a default for an Attribute (doesn't have to be a parameter)

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f'{self.year} {self.make} {self.model}'
        print(longName.title())

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f'This car has {self.odometerReading} miles on it.')

    # Modifying an attribute’s Value through a Method:
    def updateOdometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # Incrementing an attribute’s Value through a Method:
    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading. """
        self.odometerReading += miles 

myNewCar = Car('audi', 'a4', 2016)  #make in instance from Car and store it in variable myNewCar
myNewCar.getDescriptiveName()
myNewCar.readOdometer()
# myNewCar.odometerReading = 23 # Modifying an attribute’s Value Directly through an instance
# myNewCar.readOdometer()
myNewCar.updateOdometer(23) # 23 would be an argument 
myNewCar.readOdometer()
# Incrementing an attribute’s Value through a Method:
myUsedCar = Car('subaru', 'outback', 2013)
myUsedCar.getDescriptiveName()
myUsedCar.updateOdometer(23500)
myUsedCar.readOdometer()
myUsedCar.incrementOdometer(100)
myUsedCar.readOdometer()



# try it yourself 
class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type 
        self.numberServed = 0

    def describe_restaurant(self):
        print(f'{self.name} is beautiful and is a {self.type} of place.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')

    def currentNumberServed(self):
        print(f'We have served {self.numberServed} people')
    
    def totalNumberServed(self, total):
            self.numberServed = total

    def incrementNumberServed(self, served):
        self.numberServed += served
        

place = Restaurant('Popbelly', 'Mexican')
place.totalNumberServed(3)
place.currentNumberServed()
place.incrementNumberServed(100)
place.currentNumberServed()


# 3) inheritance 
# The __init__() Method for a Child Class
# car example from above 
"""A class that can be used to represent a car.""" # use a docstring that briefly describes the contents of this module.
class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model 
        self.year = year 
        self.odometerReading = 0   # setting a default for an Attribute (doesn't have to be a parameter)

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f'{self.year} {self.make} {self.model}'
        print(longName.title())

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f'This car has {self.odometerReading} miles on it.')

    # Modifying an attribute’s Value through a Method:
    def updateOdometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # Incrementing an attribute’s Value through a Method:
    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading. """
        self.odometerReading += miles 

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # special function that helps Python make connections between the parent and child class.
        self.batterySize = 70 # Defining Attributes and Methods for the Child Class

    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This cas has a {self.batterySize} -kwk battery." )

myTesla = ElectricCar('tesla', 'model s', 2016)
myTesla.getDescriptiveName()
myTesla.describeBattery()


#  4) try it yourself page 185