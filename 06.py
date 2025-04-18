# this is a list of different data types in python.
# list is used to store multiple data types in a single variable.
# list are mutable i.e. they can be changed once declared.

list1 = ["Shubh",123,12.56,True, None]
print(list1)
print(type(list1))
print(list1[0]) # this will print the first element of the list

list1[0] = "fenil" # this will change the first element of the list
print(list1)

print(list1[0:3]) # this will print the elements from 0 to 2 index this is called list slicing
print(list1[-1]) # this will print the last element of the list


# LIST METHODS

list1.append("het") # this will add the element at the end of the list
print(list1)

list2 = [34,67,56,2,10,46]
list2.sort()
print(list2)
list2.reverse() # this will sort the list in ascending order
print(list2)
list2.insert(2,100) # this will insert the element at the given index
print(list2)
list2.pop(2) # this will remove the element at the given index
print(list2)
list2.remove(10) # this will remove the given element from the list
print(list2)
list2.clear() # this will clear the list
print(list2)

# there are many more functions in python for lists like count, index, copy, etc. use chatgpt to know more about them.
