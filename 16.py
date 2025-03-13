# a = int(input("Enter the number:")) this is the prgram to print the table of the number with f string
 
# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")
    


l = ["Harry" , "Sohan" , "Sachin" , "Rahul"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}") # print("Hello",name)  we can also use this 



a = int(input("Enter the number:"))
i = 1 
sum  = 0 
while(i<=a):
    sum = sum + i
    i = i + 1

print(sum)
