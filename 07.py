# tuples in python 
# tuples are similar to lists but they are immutable i.e. they cannot be changed once declared.

a = (1,2,3,4,5,6)
print(a)
print(type(a))
b = (1,) # this is a tuple with only one element
print(b)
print(type(b)) 


# tuple methods

print(a.count(1))  # this will count the number of times the given element is present in the tuple
print(a.index(3))  # this will return the index of the given element
print(len(a)) # this will return the length of the tuple