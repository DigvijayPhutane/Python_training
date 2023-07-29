""""""
"""
 
rows= 5
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0,-1):
    for j in range(0, i-1):
        print("*", end=' ')
    print("\r")
____________________________________________
"""




for outer in range(15): # rows
     for inner in range(7): # columns
         #print(outer,inner,end='\t\t')
         if (outer==0 and inner==3) or (outer==5 and inner in [0,1,2,4,5,6]) or (outer==9 and inner in [2,4]) or(outer==14 and inner in [1,5]):
             print('**', end='\t\t')
         else:
             print('..',end='\t\t')
     print()
