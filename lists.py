#Creating a list
my_first_list= [1,2,3,4,5]
# Accessing elements
print("First", my_first_list[0])
print("Last", my_first_list[-1])
#Can also be used as an alternative to last when the number of elements are known
print("Last_Alt", my_first_list[4])
#Can also be used as an alternative to first when the number of elements are known
print("First_Alt", my_first_list[-5])

#Modifying Elements
my_first_list[3]= 10
print("Modified list" , my_first_list)

#Adding elements and removing elements ie. the values
my_first_list.append(6)
print ("List after appending: ", my_first_list)
my_first_list.remove(2)
print("List after removing", my_first_list)

#Accepting a list from a user and printing
#The method below takes the arguments as a string
string= input("Enter elements seperated by space")
my_list1= string.split()
#in the following we convert num to an int type or else it is string
my_list1=[int(num) for num in my_list1]
print("list: ", my_list1)

#A loop can also be used to accept values
#for loop is used when number of elements are known
# n is the number of elements here defined by the user
#n = input("Enter the number of elements:")
#my_list2= []

#for a counter i from 0 to n, enter an elements with i increasing by 1
#for i in range(n):
# element= input("Enter Element {}".format(i+1))
#my_list2.append(element)
#print("List", my_list2)



