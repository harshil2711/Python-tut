class A:
    def met(self):
        print("Class A method")
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met()

# Output
# Class A method

