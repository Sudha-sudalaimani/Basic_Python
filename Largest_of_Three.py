#3.	Find the largest of three numbers.
#one way
a=10
b=20
c=12

print("The Larger number is:",max(a,b,c))

#Another Way
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>=b and a>=c:
    print(" a is large number")
elif b>=a and b>=c:
    print("b is large number")
else:
    print("c is large number")
