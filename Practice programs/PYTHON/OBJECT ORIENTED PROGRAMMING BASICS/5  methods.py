# methods explained
"""
types are
Instance methods
class methods
static methods
"""


class Student:
    school = "Telusko"

    # examples for instance methods are given

    def __init__(self, m1, m2, m3):  # constructor
        self.m1 = m1  # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        self.sw = 7
        return (self.m1 + self.m2 + self.m3) / 3

    """
    instance methods generally divided into two types 
    1. accessors methods [ gets value]
    1. mutators methods [ sets value]
    """

    # accessor method to get a variable
    def get_m1(self):
        return self.m1

    # mutator method to change the value of a variable
    def set_m1(self, value):
        self.m1 = value

    # actually we can access and change variable directly
    # with (s1.m1)
    # but people some time prefer using methods
    """ class methods """

    @classmethod  # decorator used to tell next method is class method
    def info(cls):  # instead of self we use "cls" for class variables
        print("cls.school")  # class method will use class variables
        return cls.school

    # above is class method
    # we used @classmethod some thing that is called as decorator
    # used to tell next method is class method
    # class methods use class variables
    """ stacic methods """

    # static methods
    # it had nothing to do with both instance and class methods
    # we will use decorator @static method
    @staticmethod
    def info1():  # we will not use self and cls
        print("this is student class")


s1 = Student(12, 525, 56)
s2 = Student(13, 356, 546)

print(s1.avg())
print(s2.avg())
s1.sw = 243
print(s1.sw)

print(Student.info())
print(Student.info1())