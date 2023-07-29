a = [1,2,3,4,5,6,7,8]
b = [3,4,5,6,7,8,9,0]
com_list = []
for i in a:
    if i in b:
        com_list.append(i)
print(com_list)