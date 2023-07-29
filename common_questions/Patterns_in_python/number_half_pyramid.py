def number_half():
    num = 1
    n = int(input("enter the number: "))
    for i in range(n):
        for j in range(i+1):
            print(num, end = " ")
            num += 1
        print()
number_half()