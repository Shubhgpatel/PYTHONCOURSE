# Loops in python
# we can use for loop to iterate over a list, tuple, string etc.
# we can use while loop to iterate over a list, tuple, string etc.

for i in range(0,30,5): #for loop
    print(i)
 

print("WHILE LOOP")
i=10
while(i<20): #while loop
    print(i)
    i+=1

print("PRINTING THE LIST ELEMENTS")
list1 = [1,2,3,4,5]
i=0
# while(i<len(list1)):
#     print(list1[i])
#     i+=1

for i in list1: 
    print(i)
else: 
    print("Done") # this will be executed after the loop is exhausted