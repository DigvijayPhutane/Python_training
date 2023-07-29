
prime=[]
for num in range(2,101):
    for divisor in range(2,num):
        if num % divisor == 0:
            break
    else:
        prime.append(num)
print(prime)