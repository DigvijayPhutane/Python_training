""""""
"""

nm = ['ankit' , 'shivansh' , 'amit' , 'devansh']
# generate a new list with uppercase names

up = lambda n: n.upper()

print(list(map(up,nm)))

#fetch names ending with 'sh'

print(list(filter(lambda name:name.endswith('sh'),nm)))
___________________________________________________________

sal = [23000, 45000, 56000, 60000]
# generate a new list of salary with 10% bonus

bonus = lambda amt:amt +amt*.1

print(list(map(bonus,sal)))
__________________________________
"""
#why lambda is nameless

'''sal = [23000,45000,56000,60000]
# generate a new list of salary with 10% bonus

# we can directly supply a lambda function in HOF
print(list(map(lambda amt:amt+ amt*.1,sal)))'''
'''
nm = ['ankit' , 'shivansh' , 'amit' , 'devansh']
# generate a new list with uppercase names

up = lambda n: n.upper()

print(list(map(up,nm)))'''
'''lis1 = ["rit","maya","dig"]
up = lambda n : n.upper()
print(list(map(up,lis1)))
'''
'''x = lambda a,b : a*b
print(x(5,6))'''

def myfuct(n):
    return lambda a:a*n
mmy = myfuct(2)
print(mmy(11))