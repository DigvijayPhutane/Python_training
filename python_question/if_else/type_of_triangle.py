#equilateral = same side
#iso = two side same
#scalen = diffrent three side
a = int(input())
b = int(input())
c= int(input())
if a==b==c:
    print("ITS A EQUILATERAL TRIANGLE")
elif a!=b!=c:
    print("ITS A SCALENE TRIANGLE")
else:
    print("ITS A ISOSCELES TRIANGLE")