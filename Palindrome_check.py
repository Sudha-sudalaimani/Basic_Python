#Write a function to check if a string is a palindrome.
def Palindrome_check(word):
    if word==word[::-1]:
        print(f"{word} is Palindrome")
    else:
        print(f"{word} is not a palindrome")

Palindrome_check("noon")
