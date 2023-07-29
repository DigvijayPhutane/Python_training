'''a = [1,22,33,44,5,5,6,7,8]
b = [1,2,3,4,5,6,7,8,9,0]
diff = []
for i in a:
    if i not in b:
        diff.append(i)

print(diff)
'''
a = [1,22,33,44,5,5,6,7,8]
b = [1,2,3,4,5,6,7,8,9,0]
diff = list(set(a)-set(b))
print(diff)