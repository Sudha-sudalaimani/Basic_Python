#Swap the values of two variables.
#first Way
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)

##Another Way
a=10
b=20
a,b=b,a
print('a:',a)
print("b:",b)
