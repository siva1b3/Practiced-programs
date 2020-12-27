class Node:
    def __init__(self, data, next1):
        self.data = data
        self.next = next1


class Circular_Linked_list:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_in_beginning(self, data):
        self.insert_element_with_index(0, data)

    def insert_at_end(self, data):
        self.insert_element_with_index(self.size, data)

    def insert_element_with_index(self, index, data):
        if index > self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        self.size += 1
        if index == 0:
            self.head = Node(data, self.head)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
            if current.next is None:
                current = self.head
                for i in range(self.size - 1):
                    current = current.next
                current.next = self.head

    def print_val(self):
        current = self.head
        for i in range(self.size):
            print(current.data)
            current = current.next


linked_list = Circular_Linked_list()


def trail():
    linked_list.insert_element_with_index(0, 89)
    linked_list.insert_element_with_index(0, 34)
    linked_list.insert_element_with_index(0, 23)
    linked_list.insert_in_beginning(99)
    linked_list.insert_at_end(10)
    linked_list.print_val()


if __name__ == "__main__":
    trail()
