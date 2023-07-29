string = input("Enter the string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
for char in string:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found.")
