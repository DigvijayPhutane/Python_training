n = int(input())

for i in range(2,n*10+1):
    if n == 2 :
        print("prime")
        break
    elif n<= 1 or n%i == 0:
        print("NOT PRIME")
        break
    elif n%1==0 and n%n==0:
        print("prime")
        break