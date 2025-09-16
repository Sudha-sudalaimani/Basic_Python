#1.	Find the length of a string without using the len() function.
word=input("Enter a String: ")
count=0
for i in word:
    count+=1
print(f"The length the string is {count}")
