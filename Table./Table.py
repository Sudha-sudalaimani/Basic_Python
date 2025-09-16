#Print the multiplication table for a given number(For,while).
#Using For Loop
num=int(input("Enter a number:"))
for i in range(1,11):
    print(i,"x",num,"=",num*i)

#using while loop
num=int(input("Enter a number:"))
i=1
while i<=10:
    print(i,"x",num,"=",num*i)
    i=i+1
