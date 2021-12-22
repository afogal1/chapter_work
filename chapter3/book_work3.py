# using individual values from a list 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
message1 = "\nMy second bicycle was a " + bicycles[1].title() + ".\n"
print(message)
print(message1)

# modifying elements in a list 
motorcycles =  ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list using append 
motorcycles =  ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# inserting elements into a list 
motorcycles =  ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')     # inserts the value 'ducati' at the begining of the list 
print(motorcycles)

# removing elements from a list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]      # use del to remove item from list
print(motorcycles)

# removing an item using the pop() method 
motorcycles =  ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop()   # pop a value from the list and store that value in the variable popped_motorcycle
print(motorcycles)
print(popped_motorcycle)    # to prove that we still have access to the value that was removed

# popping items from any position in a list 
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)    # popping the first motorcycle in the list
print('\nThe first motorcycle I owned was a ' + first_owned.title() + '.') # print message about that motorcycle 

# removing an item by value 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')    # to find 'ducati' in the list and remove that element 
print(motorcycles) 

# example
guests = ["brad", "nick", "brandon"]
for guest in guests:
    print(f"You are invited to my party {guest.title()}")
guests[0] = "carl"
print(guests)
for guest in guests:
    print(f"You are invited to my party {guest.title()}")



