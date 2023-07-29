a = [1,2,3,4,5,6,7,8,9,0]
n = int(input())
count = 0
while True:
    if n in a:
        print(f"number {n} found at {a.index(n)}")
        break

