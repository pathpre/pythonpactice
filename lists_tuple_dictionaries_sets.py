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

