# Creating a tuple which is an immutable list
tuple1= (1,3,5,7)

#Accessing elements from a tuple
print("first: ", tuple1[0])
print("last: ", tuple1[-1])

# Creating a tuple with user inputs

string= input("Creating a user tuple")
tuple2= string.split()
tuple2= [int(num) for num in tuple2]
print("The new tuple is", tuple2)