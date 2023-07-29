#7. Write a Python program to check if a string is an anagram of another string.
string1 = input("enter the string1: ")
string2 = input("enter the string2: ")
count = 0
for i in string1:
    if i in string2:
        count += 1
    else:
        count = 0
if count == len(string1):
    print("anagram")
else:
    print("not anagram")


