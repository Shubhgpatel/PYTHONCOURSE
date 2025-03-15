# readlines method reads all the lines of a file and returns a list of strings where each string is a lin from the file.

f = open("file1.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


line = f.readline()
while (line != ''):
    print(line, end = '')
    line = f.readline()

f.close()