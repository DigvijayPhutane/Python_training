a = [1,2,3,4,5,6,7,8,9,0]
for i in a:
    if i % 3 == 0:
        a.remove(i)
print(a)