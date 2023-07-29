a = [2,4,6,8,22,20,10,18,16]
count=0
for i in a:
    if i % 2 == 0:
        count += 1
if count==len(a):
    print("ALL ARE EVEN")
else:
    print("ALL ARE NOT EVEN")