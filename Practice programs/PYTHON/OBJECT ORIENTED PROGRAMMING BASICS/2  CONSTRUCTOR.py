class computer:
    a=0
# constrotor in python with no argument
    """
    def __init__(self):
        print("in init")
    """
# constructor with two arguments
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print(cpu,ram," in init")
    def config(self):
        print(" 15 , 16gb ,1tb ",end="")
        print(self.cpu,self.ram,"in config")

com1= computer(12,23)
com2 = computer(14,1233)

com1.config()
com2.config()

