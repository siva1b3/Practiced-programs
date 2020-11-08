"""
CLASS INSIDE A:
    CLASS

    WE CAN ACCESS ELEMENTS AND METHODS OF INNER CLASS BY CREATING INNER CLASS OBJECTS
    1. WE CAN CREATE INNER CLASS OBJECTS IN OUTER CLASS
        WE CAN USE INNER CLASS METHODS AND VARIABLES IN OUTER CLASS
    2. WE CAN CREATE INNER CLASS OBJECTS BY USING OUTER CLASS OBJECTS
        WE CAN USE INNER CLASS METHODS AND VARIABLES
        BY USING INNER CLASS OBJECTS CREATED BY OUTER CLASS OBJECTS
    3. WE CAN CREATE INNER CLASS OBJECTS WITHOUT USING OUTER CLASS OBJECTS
"""


# class laptop was inside the class Student
# class laptop is called inner class
# class Student is called outer class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        """
        1. WE CAN CREATE INNER CLASS OBJECTS IN OUTER CLASS
            WE CAN USE INNER CLASS METHODS AND VARIABLES IN OUTER CLASS
        """
        self.lap = self.laptop()  # creating laptop object in Student class
        # inner class objects can be created in outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()  # inner class method used in outer class

    class laptop:
        # creating inner class in outer class
        def __init__(self):
            self.brand = "dell"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            # creating inner class method with same name as outer class method
            # it is still works even with same name
            # because it is in inner class
            print(self.brand, self.cpu, self.ram)

    def siva123(self):
        print("fhsdgh")


s1 = Student('siva', 2)
s2 = Student('naga', 3)

print(s1.name, s1.rollno)
s1.show()
s1.siva123()
"""    
2. WE CAN CREATE INNER CLASS OBJECTS BY USING OUTER CLASS OBJECTS
    WE CAN USE INNER CLASS METHODS AND VARIABLES 
    BY USING INNER CLASS OBJECTS CREATED BY OUTER CLASS OBJECTS
"""
# creating laptop object inside student class
lap1 = s1.lap
lap2 = s1.lap
# accessing inner class variables
# accessing laptop class variables
print(s1.lap.brand)
print(id(lap1))
print(id(lap2))
"""
3. WE CAN CREATE INNER CLASS OBJECTS WITHOUT USING OUTER CLASS OBJECTS
"""
# creating inner class object without using outer class
# creating laptop class without student class
lap3 = Student.laptop()
