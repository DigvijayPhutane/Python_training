'''
class MyClass():
    x = 5
p1 = MyClass()
print(p1.x)
'''

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("john",25)
print(p1.name)
print(p1.age)