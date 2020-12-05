class Stack:
    def __init__(self, capacity=None):
        self.stack1 = []
        self.capacity = capacity

    def push(self, appendvalue):
        if self.capacity != None:
            if len(self.stack1) < self.capacity:
                self.stack1.append(appendvalue)
                return True
            else:
                print("Stack is full")
                return False
        else:
            self.stack1.append(appendvalue)
            return True

    def pop(self):
        if len(self.stack1) == 0:
            print("Stack is empty")
            return False
        else:
            return self.stack1.pop()

    def peek(self):
        if len(self.stack1) == 0:
            print("Stack is empty")
            return False
        else:
            return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def is_full(self):
        if self.capacity != None:
            return len(self.stack1) == self.capacity
        else:
            return False

    def printall(self):
        print(self.stack1)


if __name__ == "__main__":
    a = Stack()
    a.push(233)
    a.push(45)
    a.push(67)
    a.push(89)
    a.push(456)
    a.push(987)
    a.push(654)
    a.printall()
    print(a.is_full())
    print(a.peek())
    print(a.pop())
    print(a.pop())
    print(a.is_empty())
    b = Stack(5)
    b.push(12)
    b.push(23)
    b.push(34)
    b.push(45)
    b.push(56)
    b.push(67)
    b.push(78)
    print(b.peek())
    print(b.pop())
    b.printall()
