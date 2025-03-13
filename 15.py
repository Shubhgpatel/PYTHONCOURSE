# Break statement, continue statement, pass statement in python 
# break statement is used to exit the loop
# continue statement is used to skip the current iteration
# pass statement is used to do nothing

for i in range(30):
    if(i==15):
        break
    print(i)

for i in range(30):
    if(i==15):
        continue
    print(i)

for i in range(30):
    pass #this pass statement will pass the loop and continue the next iteration

i = 1
while(i < 10):
    print(i)
    i += 1 
