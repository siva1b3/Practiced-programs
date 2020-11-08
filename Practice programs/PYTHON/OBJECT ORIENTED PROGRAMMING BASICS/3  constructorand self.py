"""
classs has:
    variables
    methods
"""
class computer:
    def __init__(self):
        self.age = 24
        self.name = "siva"

    def update(self):
        self.age = 30

    def compareage(self,other):
        if self.age== other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()
print(id(c1))
print(id(c2))
# above line will print address
print(c1.name)
print(c2.name)

c1.name = "naga"

print(c1.name)
print(c2.name)
print("age")
print()
print()
print(c1.age)
print(c2.age)

c1.update()

print(c1.age)
print(c2.age)
c1.age=24

if c1.compareage(c2):
    print("they are same")
else:
    print("they are not same")
