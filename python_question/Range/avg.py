start = int(input())
end= int(input())
suma = 0
count= 0
for i in range(start,end+1):
    suma += i
    count +=1
avg = suma/count
print(avg)