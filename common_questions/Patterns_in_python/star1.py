for outer in range(15):
  for inner in range(9):
     if (outer ==0 and inner==4) or (outer ==3 and inner in [1,2,3,5,6,7]) or (outer ==7 and inner in [2,6]) or (outer ==10 and inner in [1,2,3,5,6,7]) or (outer ==14 and inner==4):
        print("**",end='\t\t') #04 - 31 32 33 35 36 37 - 72 76 - 101 102 103 105 106 107 -144
     else:
        print(" ",end='\t\t')
  print()
  