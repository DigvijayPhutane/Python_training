def inverted_full():
    n = int(input("enter the number: "))
    for i in range(n):
        for s in range(i):
            print(" ", end="")
        for i in range(i,n):
            print("*",end = " ")
        print()
inverted_full()