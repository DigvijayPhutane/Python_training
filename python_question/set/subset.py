a = {1,2,3,4,5,6}
b = {1,2,3,4,5,6,7,8,9,0}
"""count = 0
for i in a:
    if i in b:
        count += 1
if len(a) == count:
    print("it is a subset")
else:
    print("IT IS NOT SUBSET")"""\

if a.issubset(b):

    print("YES IT IS A SUBSET")
else:
    print("IT IS NOT")