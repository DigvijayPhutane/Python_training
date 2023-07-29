def inverted_star():
    n = int(input("enter the number: "))
    for i in range(n):
        for j in range(i,n):
            print("*",end = " ")
        print()
inverted_star()