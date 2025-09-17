act_num=int(input("Enter a number:"))
num=act_num
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(f"{act_num} reversed as {rev}")
