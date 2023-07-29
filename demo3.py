


val = []
#val.sort(self,key,reverse,*Arg,**kwargs)       #       *Arg,**kwargs  (optional params)

#self == current object ref..
#key --> which function will tell me how to sort
#reverse -- True --> DESC ---> False -- Asc
#*Arg --> 0 to n params --> tuple
#**kwargs --> 0 to n params -- dict



for outer in range(1,6):

    for inner in range(1,6):

        if outer==1 or inner==1 or inner==5 or outer==5:
            print('*',end='\t\t')
        else:
            print(" ",end='\t\t')

    print()


import sys
sys.exit(0)

def m1():
    for outer in range(1,6):
        for inner in range(1,6):
            print(outer, inner)
            if outer == 3:
                return
        print('---------------------------')

    print('hi.....')


x = m1()   # caller --> calling of m1


import sys
sys.exit(0)


for item in range(1,21):
    if item % 4 == 0:
        continue
    print(item)



#for item in range(1,10,1):
#    print(item) # 1 2 3 4



import sys
sys.exit(0)
print('Number of Iterations Fixed ....')
numbers = []
for item in range(5):          # 0  to 19 numbers...  fix -- 20 iterations...
  num = int(input('Enter Number : '))
  if num%2==0:
      numbers.append(num)

print('For Numbers..',numbers)

print('Number of Iterations not Fixed ....')
numbers = []
while len(numbers)<5:      #Not Sure
    num = int(input('Enter Number : '))
    if num % 2 == 0:
        numbers.append(num)

print('While Numbers..',numbers)

import sys
sys.exit(0)  # stop the execution --. interprete

num = int(input('Enter Number : '))

if num <10:
    print('inside -- if -- less than 10')
elif num >=10 and num<20:
    print('inside num 10-20')
elif num>=20 and num<30:
    print('inside num 20-30')
else:
    print('inside else...')