# Sets

# Sets are unordered collections of unique elements. Sets are mutable(changeable) but the elements inside a set must b immutable. Sets are written with curly brackets.
# Sets cannot have duplicate elements.

S = {1,2,3,4,5,6,4,5,4} # this is a set and also when we print this, it will remove the duplicate elements.
print(S) 
print(type(S))
s1 = set([1,2,3,4,5,6]) # this is also a set
print(s1)
s2 = set() # this is an empty set



# Set Methods

# Define two sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Performing all operations

# 1. add(x)
s1.add(10)
print("After add:", s1)  # {1, 2, 3, 4, 5, 10}

# 2. remove(x)
s1.remove(10)
print("After remove:", s1)  # {1, 2, 3, 4, 5}

# 3. discard(x)
s1.discard(5)
print("After discard:", s1)  # {1, 2, 3, 4}

# 4. pop()
popped_element = s1.pop()
print("Popped element:", popped_element)
print("After pop:", s1)

# 5. clear()
temp_set = s1.copy()
temp_set.clear()
print("After clear:", temp_set)  # set()

# 6. union(set2)
print("Union:", s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8}

# 7. update(set2)
s1.update(s2)
print("After update:", s1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Reset s1
s1 = {1, 2, 3, 4, 5}

# 8. intersection(set2)
print("Intersection:", s1.intersection(s2))  # {4, 5}

# 9. intersection_update(set2)
s1.intersection_update(s2)
print("After intersection_update:", s1)  # {4, 5}

# Reset s1
s1 = {1, 2, 3, 4, 5}

# 10. difference(set2)
print("Difference:", s1.difference(s2))  # {1, 2, 3}

# 11. difference_update(set2)
s1.difference_update(s2)
print("After difference_update:", s1)  # {1, 2, 3}

# Reset s1
s1 = {1, 2, 3, 4, 5}

# 12. symmetric_difference(set2)
print("Symmetric Difference:", s1.symmetric_difference(s2))  # {1, 2, 3, 6, 7, 8}

# 13. symmetric_difference_update(set2)
s1.symmetric_difference_update(s2)
print("After symmetric_difference_update:", s1)  # {1, 2, 3, 6, 7, 8}

# Reset s1
s1 = {1, 2, 3, 4, 5}

# 14. issubset(set2)
print("Is subset:", s1.issubset(s2))  # False

# 15. issuperset(set2)
print("Is superset:", s1.issuperset(s2))  # False

# 16. isdisjoint(set2)
print("Is disjoint:", s1.isdisjoint(s2))  # False

