# example for single LEVEL inheritance
# means one class inherits from other one class
"""
inheritance B inherits A
            c inherits B in turn C also inheriting from A
"""


class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B(A):
    # B inherits from A
    # B can use all the methods and variables from A
    def feature3(self):
        print("3 is working")

    def feature4(self):
        print("4 is working ")


class C(B):
    # C inherits from B
    # C can use all the methods and variables from B
    # as B inherits A , C can also use all the methods and variables from A
    def feature5(self):
        print("5 is working")


s1 = A()
s1.feature1()
s1.feature2()

b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()

c1.feature1()
c1.feature3()


# EXAMPLE FOR MULTIPLE LEVEL INHERITANCE
# MEANS ONE CLASS INHERITS FROM TWO OR MORE CLASS
class D:
    def feature6(self):
        print(" feature 6 is working")

    def feature7(self):
        print(" feature 7 is working")


class E:
    def feature8(self):
        print(" feature 8 is working")

    def feature9(self):
        print(" feature 9 is working")


class F(D, E):
    # class F inherits from both classes D and E
    # class F is example of multiple inheritance
    # F can use all the methods and variables from both D and E
    def feature10(self):
        print(" feature 10 is working")


f1 = F()

# f1 object can use all the methods from D and E classes

f1.feature6()
f1.feature8()
f1.feature10()
