"""
METHOD OVERLOADING MEANS CREATING TWO METHODS WITH SAME NAME
BUT HAVING DIFFERENT TYPES OR NUMBER OF ARGUMENTS
"""

# THIS TYPE METHOD OVERLOADING IS POSSIBLE
# IN JAVA, C++, JS BUT NOT IN PYTHON
# HENCE IN PYTHON THERE IS NO METHOD OVER LOADING
# IN PYTHON WE CANT CREATE TWO METHODS OF SAME NAME
# IN SAME CLASS IN PYTHON
# BUT WE CAN TRY SOME OTHER METHODS AS SHOWN IN VIDEO

"""
EXAMPLE FOR METHOD OVERLOADING 
BUT NO BY CREATING MORE METHODS WITH SAME NAME
"""


class threearguments:
    def sum(self, argument1=None, argument2=None, argument3=None):
        if argument1 != None and argument2 != None and argument3 != None:
            summation = argument1 + argument2 + argument3
        elif argument1 != None and argument2 != None:
            summation = argument1 + argument2
        else:
            summation = argument1
        return summation


a = threearguments()

# we can run same method with different number of arguments
# which is called as method overloading

print(a.sum(112, 2, 3))
print(a.sum(12, 8))
print(a.sum(23))


