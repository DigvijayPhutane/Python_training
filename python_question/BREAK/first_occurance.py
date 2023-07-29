a = [1,2,3,4,5,1,6,7,8]
n = int(input())
for index,i in enumerate(a) :
    if i == n :
        print(f"found at:{index} position")
        break

'''fount = False
for index,num in enumerate(a):
    if num == n:
        print("target fount")
        fount = True
        break
if not fount:
    print("not found")
'''

