start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

largest_palindrome = None

for num in range(end, start - 1, -1):
    if str(num) == str(num)[::-1]:
        largest_palindrome = num
        break

if largest_palindrome is not None:
    print("Largest palindrome number:", largest_palindrome)
else:
    print("No palindrome number found in the given range.")
