# File handling in Python 
# Python has several functions for creating, reading, updating, and deleting files.
# python has a built-in function open() to open a file. it takes two parameters, the file name and the mode.

f = open("file.txt")
data = f.read()
print(data)
f.close()
