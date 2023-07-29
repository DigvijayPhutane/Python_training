def star():
  for outer in range(15):  #inner column outer row
    for inner in range(8):
      #print(outer,inner,end="\t\t") #identify point 0,3,5->3,
      #(0,3),(5,0),(5,3),(5,5),(5,7),(9,2),(9,4),(14,1),(14,5)
      if (outer ==0 and inner==3) or (outer==5 and inner in [0,1,2,4,5,7]) or (outer==9 and inner in [2,4]) or (outer==14 and inner in [1,5]):
        print("**",end='\t\t')
      else:
        print(" ",end='\t\t')
    print()
star()