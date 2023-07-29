for outer in range(7): # rows
    for inner in range(8): # columns
        #print(outer,inner,end='\t\t')
         if (outer==0 and inner in[0,1,2,3,4,5,6]) or (outer in[1,2,3,4,5,6]and inner==6 ) or(outer==6 and inner in[1,2,3,4,5,6])or(outer in[0,1,2,3,4,5,6] and inner==0):
               print('**',end='\t\t')
         else:
               print(' ', end='\t\t')
    print()