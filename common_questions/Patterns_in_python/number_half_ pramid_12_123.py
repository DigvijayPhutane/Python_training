def half_12_123():
    num = 1
    n = int(input("enter the number: "))
    for i in range(n):
        for j in range(i+1):
            print(num,end = " ")
            num = num+1
        num = 1
        print()
half_12_123()
