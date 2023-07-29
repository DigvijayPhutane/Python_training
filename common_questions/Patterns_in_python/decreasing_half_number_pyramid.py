def decreasing_pyramid():
    num = 1
    n = int(input())
    for i in range(n):
        for j in range(n,i,-1):
            print(num,end=" ")
            num = num + 1
        num = 1
        print()
decreasing_pyramid()