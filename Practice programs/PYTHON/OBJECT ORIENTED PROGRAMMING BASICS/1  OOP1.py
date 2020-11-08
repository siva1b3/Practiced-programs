class computer:
    a=0
    def config(self):
        print(" 15 , 16gb ,1tb")


a = 0
print(type(a))

com1 = computer()
print(type(com1))
"""
# how to use method in computer class
# computer.config(self)
# self means which ever object that you were using to call the method in class
"""
computer.config(com1)
# can also write as
# simple shortcut is
com1.config()
# 19,16 both are same
com2=computer()
print(type(com2))
com1.a=23
com2.a =4534535
print(com1.a)
print(com2.a)



