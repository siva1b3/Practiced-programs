"""
CONSTRUCTOR IN INHERITANCE
"""
class A:
    def __init__(self):
        print("in a init")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B:
    def __init__(self):
        print("in b init")

    def feature1(self):
        print("3B is working")

    def feature4(self):
        print("4 is working ")


class C(B, A):
    # C INHERITS BOTH A AND B
    # B WILL GET PREFERENCE OVER A WHILE USING SUPER FUNCTION
    # LEFT TO RIGHT PREFERENCE IS TAKEN AUTOMATICALLY
    def __init__(self):
        print("in c init")
        super().feature1()


a1 = C()

a1.feature1()
