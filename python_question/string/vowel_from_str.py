#4. Write a Python program to remove all the vowels from a string.
str1 = input("Enter the string: ")
vovel = "aeiouAEIOU"
vovless =''
for i in str1:
    if i not in vovel:
        vovless += i
print(vovless)



