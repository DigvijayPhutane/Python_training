""""""
"""
Function
#declaration
pass

def function_name():
    pass

function_name()
__________________________________________

def sample(*args):
    print(args)
sample()
sample(1,2,3)
sample(30,5.6,88,9)
__________________________________

def sample(**kwargs):
    print(kwargs)
sample()
sample(name='shivansh', age=5, place='pune')
____________________________________________________-

#normal function:
#add of 2 num using a normal function
def add(num1,num2):
    return num1+num2
print(add(500,300))
______________________________________

def sample(x,y):
    return x+y,x-y,x/y
print(sample(20,2))

s = lambda x,y:x+y, x-y, x/y
print(s(10,2))
#multiple expression are not allowed in lambda
_______________________________________________________________
Higher order function 
a function which takes other function as an input called as higher order function
ex. fun(func)
3 types of higher order function are their
-Map
-filter
-reduce
__________________________________________
map(fun,iterable)
map wil apply a function over each element
from an iterable
_________________________________________


num = [20,3,6,18]
# generate a new list of squared numbers from a sequence
sq = lambda num:num*num

#normal function
def square(num):
    return num*num
# supply above things in map()
print(list(map(sq,num)))
#---------------------------------------------------
print(list(map(square,num)))
___________________________________________
"""



