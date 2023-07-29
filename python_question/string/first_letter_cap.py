#6. Write a Python program to capitalize the first letter of each word in a string.
string = input("enter the string: ")
words = string.split()
for word in words:

    print(word[0].upper()+word[1:])
