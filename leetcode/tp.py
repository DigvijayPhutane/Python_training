x = int(input())
b = str(x)
if b[-1] == '0':
    b = b[:-1]
    a = b[::-1]
else:
    a = b[::-1]
print(a)