# This program writes a string to a file
# here the file is open in write mode


st = "hello world hellooooooooooooooo"
f1 = open("file1.txt", "w")
f1.write(st)
f1.close()