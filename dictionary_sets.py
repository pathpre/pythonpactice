# creating a dictionary
dict= {'name': 'Presha', 'age': '23', 'city': 'Pune'}

#Accessing Values
print("Name is", dict['name'])
print("Age is ", dict['age'])
# This is in the form of a key-value pair

# Adding a new element to an existing dictionary
dict['email']= 'presha.pathak@gmail.com'
print("updated dictionary", dict)

# Sets in Python: they are immuatable but also contain unique elements
set= {1,2,3,5,6,7,4,5}
print(set)
#Set after adding
set.add(6)
print("Set after adding 6:", set)
#Set after removing
set.remove(2)
print("Set after removing 2:", set)