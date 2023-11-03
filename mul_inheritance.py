class Root:
    def ping(self):
        print('ping from Root')
    def pong(self):
        print('pong from Root')

class A(Root):
    def ping(self):
        print('ping from A')
        super().ping()
    def pong(self):
        print('pong from A')
        super().pong()
        print('why')

class B(Root):
    def ping(self):
        print('ping from B')
        super().ping()
    def pong(self):
        print('pong from B')

class final(A,B):
    def ping(self):
        print('ping from final')
        super().ping()

class final2(B,A):
    def ping(self):
        print('ping from final')
        super().ping()

if __name__ == '__main__':
    ff = final()
    ff.ping()
    print('***********')
    ff.pong()
    print('***********')
    print(final.__mro__)
    f = final2()
    print('***********')
    f.ping()
    print('***********')
    f.pong()
    print('***********')
    print(final2.__mro__)