class Link:
    def __init__(self, data=None, next1=None):
        self.data = data
        self.next = next1


class List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Link(data)
        node.next = self.head
        self.head = node
        # can also written be in one line for convince
        # self.head = Link(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Link(data, None)
            return
        itr1 = self.head
        while itr1.next:
            itr1 = itr1.next
        itr1.next = Link(data, None)

    def print_all(self):
        if self.head is None:
            print("list is empty")
        else:
            itr = self.head
            while not itr is None:
                print(itr.data)
                itr = itr.next

    def delete_it(self):
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        temp = self.head.data
        return temp

    def find(self, data):
        itr2 = self.head
        while itr2.data != data:
            if itr2.next == None:
                print("element not found")
                return
            else:
                itr2 = itr2.next
        print("element found")

    def delete_middle(self, data):
        itr2 = self.head
        pre = itr2
        while itr2.data != data:
            if itr2.next == None:
                print("element not found")
                return False
            else:
                pre = itr2
                itr2 = itr2.next
        if self.head == itr2:
            self.head = self.head.next
        else:
            pre.next = itr2.next
        return True

    def insert_middle(self, index, data):
        itr1 = self.head
        for i in range(1, index):
            itr1 = itr1.next
        new_link = Link(data, itr1.next)
        itr1.next = new_link

    def test1(self):
        print(self.head.data)
        print(self.head.next)


if __name__ == "__main__":
    ll = List()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(99)
    ll.insert_at_beginning(998)
    ll.insert_at_beginning(959)
    ll.insert_at_beginning(949)
    ll.insert_at_beginning(939)
    ll.insert_at_beginning(929)
    ll.insert_at_beginning(199)
    ll.print_all()
    ll.insert_at_end(999)
    ll.print_all()
    print(ll.delete_it(), "deleted")
    ll.insert_at_end(996)
    ll.print_all()
    print("main")
    ll.delete_middle(929)
    ll.delete_middle(89)
    ll.delete_middle(996)
    ll.print_all()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(892)
    ll.insert_at_beginning(992)
    ll.insert_at_beginning(9938)
    ll.insert_at_beginning(9359)
    ll.insert_at_beginning(9489)
    ll.insert_at_beginning(9349)
    ll.insert_at_beginning(9629)
    ll.insert_at_beginning(1799)
    ll.insert_middle(4, 111111)
    ll.print_all()
    ll.find(23)
    print(ll.peek())
    print(ll.peek())
    ll.test1()
