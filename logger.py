# logger
# log is basically a footprint of teh actions or behaviour of the user on the software or website !
import logging
logging.basicConfig(filename='app.log',filemode='a',level=logging.DEBUG,format='') # cant be read i.c e cant be write i.e w it is A i.e append
def div(num1,num2):
    print('num1:',num1,'num2:',num2)
    try:
        result = num1/num2
    except ZeroDivisionError as z:
        print("invalid ")
    else:
        print("result",result)


count = 0
while True:
    try:
        num1 = int(input("enter num1"))
        num2 = int(input("entyer num2"))
    except ValueError as v:
        print("error")
        count = count+1
    else:
        div(num1,num2)
        count = 0
    if count == 3:
        print("3 attempts done!")
        import sys
        sys.exit(0)
    else:
        print("attempts are remaining are = ",3-count)


div(num1,num2)