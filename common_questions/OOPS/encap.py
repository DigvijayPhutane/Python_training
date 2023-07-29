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