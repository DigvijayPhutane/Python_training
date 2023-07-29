a = [1, 2, 1, 2, 1, 2, 3, 4, 5, 1, 23, 4, 5, 6]
n = int(input("Enter the element to remove: "))
nth = int(input("Enter the occurrence number: "))

count = 0
i = 0
while i < len(a):
    if a[i] == n:
        count += 1
        if count == nth:
            del a[i]
            break
    else:
        i += 1

print("Updated list:", a)