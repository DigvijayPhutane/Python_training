""""""
"""
class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project



    def show(self):

        print('name : ', self.name, 'salary:', self.salary)
    def work(self):
        print(self.name, 'is working on ', self.project)

emp = Employee('shivansh', 800000, 'NPL')

emp.show()
emp.work()
_____________________________________________________-
class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print('name: ', self.name, 'salary:', self.salary)

emp = Employee('devansh', 100000)

print('name:', emp.name, 'salary:', emp.salary)

emp.show()
__________________________________________________-

a = 100
_b = 200
__c = 20
___________________________
class sample:
      x = 20
      y = 30
      z = 40

s = sample()
print(s.x,s.y,s.z)
_______________________________
class Sample:
    x = 20
    _y = 30
    __z = 40
s = Sample()

print(s.x, s._y,)
print(dir())
________________________________________
class Test:
    def m1(self):
        print('public method')

    def _m2(self):
        print('Protected method')
        self.__m3()
    def __m3(self):
        print('Private method')

t = Test()
t.m1()
t._m2()
#t.__m3()
_____________________________
class Test:
    __pin = 1234

class Sample(Test):
    def m1(self):
        print(super().__pin)
s = Sample()
s.m1()
_____________________________________
class Test:
    __pin = 1234
    a = 10
    b = 30

t = Test()
print(dir(t))
print(t._Test__pin)# Using name mangling technique
(# syntax: obj._class__member)
_____________________________________________
class Bank:
    def __security(self):
        print('Private Security Method')

b = Bank()
b._Bank__security()
____________________________________________________
a = 1
b = 'python'
def add():
    pass
# dir() display current memory structure
print(dir())
___________________________________________________
class Test:
    a = 10
    b = 20

    def add(self):
        pass
print(dir(Test)) 
_________________________________________________
class Test:
    a = 100
    def m1(self):
        print('m1')

    def m2(self):
        print('m2')

    def display(self):
        # access a ,call m1,m2 methods
        print(self.a)
        self.m1()
        self.m2()

t = Test()
t.display()
______________________________________________________
"""
'''class sample:
    x = 8

    def m1(self):
        print('Inside using self:', self.x)
s = sample()
s.m1()
print('outside using object:', s.x)
# third reference is class name
print('Using className:', sample.x)
print(dir())
'''
''''''
class Test:
    def m1(self):
        print('public method')

    def _m2(self):
        print('Protected method')
        self.__m3()
    def __m3(self):
        print('Private method')

t = Test()
t.m1()
t._m2()
#t.__m3()

''''''
'''class base:
    def __init__(self):
        self._a = 2
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling protected member of base class",self._a)

        self._a = 3
        print("calling modified protected member of base class",self._a)

obj1 = derived()
obj2 = base()

print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

'''



