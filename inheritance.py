""""""
"""
class Tata:
    balance = 120
    def insurance(self):
        print('Insurance domain')
    def vehicles(self):
        print('Vehicles domain')
    def machines(self):
        print('Machines domain')


class TataMotors(Tata):


    def new_innovation(self):
        print('New innovations')

tm = TataMotors()
tm.vehicles()
tm.new_innovation()
______________________________________________
class Father:
    amt = 50000
    def Car(self):
        print('Father car')
class Child(Father):
    mera_paisa = 450
c = Child()
print(c.mera_paisa)
____________________________________________________
Multilevel Inheritance:
Parent<----- Child_1<-------child_2........
_____________________________________________

class Central_gov:
    def fund(self):
        print('Central fund')
class State_gov(Central_gov):
    def fund(self):
        print('State fund')
class Local_gov(State_gov):
    def fund(self):
        print('Local fund')
l = Local_gov()
l.fund()
#MRO Method resolution order
________________________________________________________

class Central_gov:
    def fund(self):
        print('Central fund')
class State_gov(Central_gov) :
    def fund(self):
        print('State fund')
        super().fund()

class Local_gov(State_gov):
    pass
l = Local_gov()
l.fund()
________________________________________________________

class State_gov:
    def fund(self):
        print('State fund')

class Local_gov(State_gov):
    def fund(self):
        print('local fund')
_____________________________________________________________
class Father:
    def money(self):
        print('Father money')
class Mother:
    def money(self):
        print('Mother money')

class Child(Mother,Father):
    pass

C = Child()
C.money()
________________________________________________________________

class A:
    x = 100
class B(A):
    x = 200
    def m1(self):
        print(super().x)
class C(B):
    pass

ob = C()
print(ob.x)
ob.m1()
__________________________________________________________

class Sample:
    def m1(self):
        print('Sample m1')

class Test(Sample):
    def m1(self):
        super() .m1()
        print('Test m1')
t = Test()
t.m1()
____________________________________________________________
"""

class Father:
    def money(self):
        print('Fathers money')
class Mother:
    def money(self):
        print('Mothers money')
class Child(Mother,Father):
    pass


c = Child()
c.money()














