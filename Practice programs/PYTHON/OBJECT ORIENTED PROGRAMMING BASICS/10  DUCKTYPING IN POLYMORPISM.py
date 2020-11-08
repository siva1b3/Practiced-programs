"""
DUCK TYPING
the thing which walks like duck
the thing which quack like duck
the thing which swim like duck
IS THE DUCK
JUST LIKE THAT
"""


class pycharm:
    def execute(self):
        print("running")
        print("compiling")


class myeditor:
    def execute(self):
        print("compling")
        print("checking")
        print("running")


class laptop:
    # here in place of ide we can use both pycharm and myeditor
    # because what we need is an object that is having execute method in it
    # is is not matter weather it is object of
    # pycharm or myeditor
    def code(self, ide):
        ide.execute()


lap1 = laptop()
ide = pycharm()  # INSTEAD OF PYCHARM WE CAN ALSO USE MYEDITOR
# BOTH CAN RUN THE EXECUTE METHOD
# SO IT DOSEN'T MATTER WHAT EVER YOU USE IT WILL MAKE WORK
lap1.code(ide)
