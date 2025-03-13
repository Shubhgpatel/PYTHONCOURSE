# Conditionals statements in python

a = int(input("Enter the age: "))

if(a>18):
    print("you're an adult")
elif(a==0):
    print("You entered a invalid age number")
elif(a<0):
    print("you're entenring a negative number")
    
else:
    print("you're a minor")

print("End of the program")



b = int(input("Enter the age:"))

if(b>=18):
    print("Yes")
else:
    print("No")