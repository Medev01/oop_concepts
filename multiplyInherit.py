class A:
    def a(self):
        print('a')


class B(A):
    def b(self):
        print("b")


class C(B):
    def c(self):
        print('c')


c1 = C()
c1.a()
