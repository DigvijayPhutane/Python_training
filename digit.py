""""""\
"""
 s = 'Laxmikant'

print(s.split())
 ______________________________________
 s = 'Laxmikant got 87 89 78 90 marks in four subjects'
#print(s.split())
for i in s.split():
     if i.isdigit():
         print(i)
"""

k = [10,-3,45,7,-56,-70,80,17,23]
# PS: Separate +ve and -ve numbers in list
p = []
n = []
for num in k:
    if num >=0:
        p.append(num)

else:
    n.append(num)
print('+ve numbers:',p)
print('-ve numbers:',n)


