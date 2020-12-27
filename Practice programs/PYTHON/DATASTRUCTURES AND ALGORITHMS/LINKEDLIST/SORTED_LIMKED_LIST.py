class Node:
    def __init__(self, data, next1):
        self.data = data
        self.next = next1


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # for normal singly linked list

    """
    def insert_at_the_beginning(self, data):
        self.insert_with_index(0, data)

    def insert_at_the_ending(self, data):
        self.insert_with_index(self.size, data)

    def insert_with_index(self, index, data):
        if index > self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        if index == 0:
            self.head = Node(data, self.head)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
        self.size += 1
    """

    def peek_top(self):
        return self.peek_index(0)

    def peek_bottom(self):
        return self.peek_index(self.size - 1)

    def peek_index(self, index):
        if index >= self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def peek_element(self, data):
        current = self.head
        while current.data != data:
            if current.next is None:
                print("element", data, "not found")
                return False
            current = current.next
        print("element", data, "is found")
        return True

    def delete_top_element(self):
        return self.delete_with_index(0)

    def delete_bottom_element(self):
        return self.delete_with_index(self.size - 1)

    def delete_with_index(self, index):
        if index >= self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        self.size -= 1
        if index == 0:
            temp = self.head
            self.head = self.head.next
            return temp.data
        current = self.head
        for i in range(index - 1):
            current = current.next
        temp = current.next
        current.next = current.next.next
        return temp.data

    def delete_with_value(self, data):
        current = self.head
        previous = current
        while current.data != data:
            if current.next is None:
                print("element", data, "not found")
                return False
            previous = current
            current = current.next
        temp = previous.next
        previous.next = current.next
        print("element", data, "is found and deleted")
        self.size -= 1
        return temp.data

    def print_val(self):
        current = self.head
        while current:
            print(current.data, "\b--->", end="")
            current = current.next
        print()


class Sorted_Linked_List(Linkedlist):
    def insert_element(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
        else:
            current = self.head
            previous = current
            while current.data < data:
                if current.next is None:
                    current.next = Node(data, current.next)
                    return True
                previous = current
                current = current.next
            if previous == current:
                self.head = Node(data, self.head)
            else:
                previous.next = Node(data, previous.next)
        self.size += 1


linkedlist = Sorted_Linked_List()


def trail1():
    linkedlist.insert_element(78)
    linkedlist.insert_element(34)
    linkedlist.insert_element(45)
    linkedlist.insert_element(899)
    linkedlist.insert_element(0)
    linkedlist.insert_element(-1)
    linkedlist.insert_element(8999999)
    linkedlist.print_val()


if __name__ == "__main__":
    trail1()
