#3. Write a Python program to check if a string is a palindrome.
str1 = input("Enter the string: ")
if str1 == str1[::-1]:
    print("It is palindrome")
else:
    print("Not a palindrome")
