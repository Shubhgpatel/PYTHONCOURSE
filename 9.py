# Dictionaries

# Dictionary is a collection of key-value pairs. it is unordered, mutable(changeable) and indexed. In python, dictionaries are written with curly brackets, and they have keys and values.
# Dictionary cannot contains duplicate keys, but it can contain duplicate values.

marks = {
    "Shubh": 100,
    "Varshil": 100,
    "het": 100,
    "list" : [1,2,3,4], # this is a list inside a dictionary
    "tuple" : (4,3,2,1) # this is a tuple inside a dictionary
}

print(marks)
print(type(marks))
print(marks["list"])
print(marks["tuple"])
print(marks["Shubh"]) # this will print the value of the key "Shubh"


# Dictionary Methods
print(marks.items()) # this will return a list of tuples containing key-value pairs
print(marks.keys()) # this will return a list of keys
print(marks.values()) # this will return a list of values
marks.update({"Shubh":99}) # this will update the value of the key "Shubh"
print(marks.get("Shubh")) # this will return the value of the key "Shubh"
print(marks)
print(marks.get("Shubh1")) # this will return None if the key does not exist
print(marks["Shubh1"]) # this will raise an error if the key does not exist