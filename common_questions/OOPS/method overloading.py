class my_class:
    def my_method(self,arg1,arg2 = None):
        if arg2 is None:
            print("one argument only",arg1)
        else:
            print("both argument",arg1,arg2)
obj = my_class()
obj.my_method("hello")
obj.my_method(('hello',"dig"))