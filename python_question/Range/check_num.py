s = int(input("start: "))
e = int(input("end: "))
r = int(input("number: "))
if r in range(s,e+1):
    print("PRESENT")
else:
    print("NOT PRESENT")