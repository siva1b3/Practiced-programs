print(int.__add__(10, 13))
print(10 + 13)
# instead of using + we are using method int.__add__
# "+" in python in turn represents int class add method(int.__add__)
a = '45'
b = '  siva'
print(str.__add__(a, b))
print(a + b)
# both the above prints will give the same answer
# instead of using + we are using method str.__add__
# " + " is an operand which represents __add__ method
# JUST LIKE THAT
# " - " is an operand which represents __sub__ method
# " * " is an operand which represents __mul__ method
# and so on ,,,,,,,...
"""
OPERATOR OVERLOADING
    MEANS WE ARE HAVING SAME METHODS BUT THE ARGUMENTS IT WILL TAKE MAY CHANGE
    TO USER DEFINED OBJECTS
    +,-,* ALL SYMBOLS WILL ONLY WORK FOR PREDEFINE CLASSES LIKE INT,STR,ETCC
    IF WE WANT TO ADD TWO USE DEFINED OBJECTS
    WE NEED TO RECREATE __add__ and __sub__ etc,,,. methods in our user defined class
    this recreation of operator methods in our user defined class is called 
    OPERATOR OVERLOADING 
    operator                    magic method
        +                   __add__(self, other)
        -                   __sub__(self, other)
        *                   __mul__(self, other)
        /                   __div__(self, other)
        <                   __lt__(self, other)
        >                   __gt__(self, other)
        >=                  __ge__(self, other)
        print               __str__()
        and so on
"""


# EXAMPLE FOR OPERATOR OVERLOADING POLYMORPHISM

class student:
    # student class has its own
    # add,sub,mul,gt(greater than) methods instead of bultin methods
    # to work with student objects
    def __init__(self, marks1, marks2):
        self.m1 = marks1
        self.m2 = marks2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        studentnew = student(m1, m2)
        return studentnew

    def __gt__(self, other):
        totalmarks1 = self.m1+self.m2
        totalmarks2 = other.m1+other.m2
        if totalmarks1>totalmarks2:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1, self.m2
        # above line can be used when we are using
        # .__str__() in the last OF PRINT LINE AS SHOWN IN LINE "96"
        # or
        # we can also use this without using __str__()
        return ' {} {} '.format(self.m1, self.m2)


student1 = student(98, 99)
student2 = student(65, 66)

# now ADD TWO STUDENT OBJECTS to create a new student object
# add by using add method in class

student3 = student1 + student2
print(student3.m1)
print(student3.m2)

# now compare two students with using symbol

if student1>student2:
    print("student1 wins")
else:
    print("student2 wins")

a=3
print(a)
print(a.__str__())
# above two lines both are same
# now how to print an object
# but to print an object we need to specify __str__ COMPULSORY
# by using __str__ method in our class

print(student1.__str__())

# INSTEAD OF USING __str__ we can return string from method

print(student1)
print(student2)