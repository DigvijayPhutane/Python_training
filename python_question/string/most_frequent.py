#8. Write a Python program to find the most frequent character in a string.
string = input("enter the string: ")
count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

mf = max(count,key=count.get)
print(mf)



