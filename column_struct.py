""""""
"""
for i in range(0,5):


   for j in range(1,i+3):
       print("*", end=" ")

print("")
for i in range(0,6):

   for j in range(1,1-3):

       print("*", end=" ")

print("")
________________________________________
def print_pascal_triangle(size):
    for i in range(0,size):
        for j in range(0,i+1):
            print(decide_number(i,j),end=" ")
        print()


def decide_number(n, k)   :
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0,k):
        num = num * (n - i)
        num = num // (i+1)
    return num
# set rows
rows = 7
print_pascal_triangle(rows)
"""
