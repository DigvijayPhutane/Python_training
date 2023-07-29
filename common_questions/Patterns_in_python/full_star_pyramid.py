def full_pyramid():
    n = int(input("enter the number: "))
    for i in range(n):
        for s in range(-n,-i):
            print(" ",end = "")
        for j in range(i+1):
            print("*",end = " ")
        print()

full_pyramid()

