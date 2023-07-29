a = [1,2,3,4,5,6,7,8,9,0]
i = 0
n = int(input())
while True:
    if n in a:
        print(f"its there in list at: {a.index(n)} position",)
        break
    else:
        print(f"not fount {n} in this list")
        break
