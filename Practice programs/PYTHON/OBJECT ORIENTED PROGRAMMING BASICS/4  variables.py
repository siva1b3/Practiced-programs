class car:
    # class variable
    wheels = 4

    def __init__(self):
        # instance variables
        self.mil = 10
        self.com = "BMW"


# on regular base both class and instance variables are works same
#
# but class methods and instance methods are working differently


c1 = car()
c2 = car()
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)

c1.mil = 8

print(c1.mil, "", c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)

car.wheels = 5
print(c1.mil, "", c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)

c1.wheels = 6
print(c1.mil, "", c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
