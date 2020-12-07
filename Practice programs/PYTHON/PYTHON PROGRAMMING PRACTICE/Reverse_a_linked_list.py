from random import randint


class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_top(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            self.tail = self.head
            self.size += 1
        else:
            self.head = Node(data, self.head)
            self.size += 1

    def print_list(self):
        itr = self.head
        while itr is not None:
            print(str(itr.data)+"-->", end="")
            itr = itr.next
        print("\b\b\b")


link_list = Linked_List()


def main():
    for i in range(12):
        k = randint(0, 12425)
        link_list.insert_top(k)
    link_list.print_list()


def trail():
    pass


def reverse_list(data1):
    new_list = Linked_List()
    while data1 is not None:
        new_list.insert_top(data1.data)
        data1 = data1.next
    new_list.print_list()


if __name__ == "__main__":
    main()
    reverse_list(link_list.head)
