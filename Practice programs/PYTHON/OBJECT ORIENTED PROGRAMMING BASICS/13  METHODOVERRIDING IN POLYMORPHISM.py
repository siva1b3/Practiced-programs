# example for method overriding
# first case shows with out program without method overriding
"""
class A:
    def show(self):
        print("its A show")


class B(A):
    pass


b1 = B()
b1.show()
"""

# in the above program it will use class A method


# with method overriding
# IN BELLOW PROGRAM IT WILL USE CLASS B METHOD
# BECAUSE SHOW METHOD IN CLASS B IS OVERRIDING
# SHOW METHOD IN CLASS A

class A:
    def show(self):
        print("its A show")


class B(A):
    def show(self):
        print("its B show overriding complete")


b1 = B()
b1.show()
