'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''
'''
class parent():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
x = parent("john", "pigo")
x.printname()

class child(parent):
    pass
y = child("Mike", "Olsen")
y.printname()

'''

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def pers(self):
        print(self.name,self.age)
p1 = person("john", "25")
p1.pers()

class student(person):
    pass
z = student("lala",30)
z.pers()

