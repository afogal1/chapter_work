steve = {
    "name": "Steve",
    "weight": 155.5,
    "height": 70,
    "foods": ["country fried steak", "fried chicken", "collards"],
    "ice_cream" : {
        "vanilla" : False,
        "chocolate" : True,
        "coffee" : False
    },
    10: "this has an integer key"
}
# name_of_dict[KEY]
print(steve["ice_cream"]["vanilla"])
print(type(steve["ice_cream"]["vanilla"]))

print(steve.get("canides", "No Candy List"))

steve.update(
    {
        "candies":["snickers", "mars", "m&ms"]})
print(steve)
# delete a list (DEL)
del steve["candies"]

for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items())
for key, value in steve.items():
    print(key, end=" ")
    print(value)


print(steve.items())
for key, value in steve.items():
    if isinstance(value,list):
        print(f"The list is at {key}")
    
steve["name"]="Joe"
print(steve)

my_list= [1,2,3]
my_list[1]="WOW"
print(my_list)

