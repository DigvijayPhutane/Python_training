
class Emp:
    company_name = 'Infosys'

    def __init__(self,eid,enm,email):
        self.emp_id = eid
        self.emp_name = enm
        self.emp_email = email

    def __str__(self):
        return f'''{self.__dict__}'''

    @classmethod                # factory method ka mhntoy --> Emp che objects...
    def create_an_emp_instance(cls,eid,enm,email):
        if eid<=0:              # Object >> --> class method --> Using Classname --> obj ??
            print('Invalid Emp Id')
        return cls(eid,enm,email)       #new --init         # init la call karel...

    def change_email(self,val):     # instance method --> instance variable la change--> obj ref
        self.emp_email = val

    @staticmethod
    def change_company_name(newname):
        Emp.company_name = newname

e1 = Emp.create_an_emp_instance(101,'Mr XXXX')
e2 = Emp.create_an_emp_instance(102,'Mr YYY')

print(e1)
print(e2)

import sys
sys.exit(0)



class Demo:


    def __init__(self):     # object --> __new__  --> object create --> __init__ --> init
                        #self  --> current object ref..     object asel.
        print('...')   # line --> 6 execution la object asel....

    def m1(self):           # self --> current object cha ref...    --> object
        print('inside m1 --> instance method',self)

    @staticmethod
    def m2():               # static method -> dont have any reserved param.. --> classname
        print('inside m2  --> static method')

    @classmethod
    def m3(cls):            # cls --> class     --> classname
        print('inside m3 --> class method')

#Demo.m1()       # NO --> first of all we need to create an instance/object then only we call m1
d1 = Demo()
d1.m1()

d2 = Demo()
d2.m1()

Demo.m3()       # class chi method
d1.m3() # not recommanded
d2.m3() # not recommanded

import sys
sys.exit(0)
def addition(*args):            # older running... --> you cannot make changes in addition function..
    print('Inside addition')
    result = sum(args)      # args -- tuple -->
    print('addition cha code written...')
    return result


def smart_addition(*args):
    print('Inside smart addition')
    sum = 0
    for item in args:
        if type(item)==int:
           sum = sum + item
    return sum

#addition = smart_addition       # monkey patching...  function


result = addition(10,20,30,40,50,'A','34',5,True)
print(result)

import sys
sys.exit(0)
class Employee:

    def __init__(self,name,age,email='xxx@gmail.com'):      # default
        self.emp_name = name
        self.emp_age = age
        self.emp_email = email

    def change_an_email(self,value):
        if value:
            self.emp_email = value
        else:
            print('Invalid Email')

    def __str__(self):
        return f'''{self.__dict__}'''

    def new_email_change_method(self,value):
        print('new_email_change_method callled...')
        if value:
            self.emp_email = value
        else:
            print('Invalid Email')

#instance = object
e1 = Employee(name='Mr ABC',age=33,email='abc@gmail.com')
print(e1)       # what wud be the value of an email  --> abc@gmail.com
e1.change_an_email("pqr@gmail.com")
print(e1)       #what wud be the value of an email      # pqr@gmail.com

e1.change_an_email = e1.new_email_change_method   #monkey patching...       # method..

print('--------------------------')
e1.change_an_email('xyz@gmail.com')