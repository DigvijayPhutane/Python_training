'''class Myclass:
    x = 5
pi = Myclass()
print(pi.x)
'''
"""
class person():
    def __init__(self,name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"


p1 = person("john",55)
print(p1) #__str__ give the memory location of the object

print(p1.name)
print(p1.age)

"""
'''
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("my frd", self.name ," is " ,self.age," years old!")

p1 = person("john",55)
p1.myfunc()
'''
class man():
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
p1 = man("john",55,5.12)
print(p1.name , p1.age , p1.height)


