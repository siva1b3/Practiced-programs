class Node:
    def __init__(self, data, reference_of_next_node):
        self.data = data
        self.reference_of_next_node = reference_of_next_node


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def length(self):
        return self.size

    def insert_at_the_beginning(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def insert_at_the_end(self, data):
        self.size += 1
        if self.head == None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.reference_of_next_node != None:
                itr = itr.reference_of_next_node
            itr.reference_of_next_node = Node(data, None)

    def insert_in_the_middle(self, index, data):
        self.size += 1
        itr = self.head
        for _ in range(index - 1):
            itr = itr.reference_of_next_node
        itr.reference_of_next_node = Node(data, itr.reference_of_next_node)

    def peek_the_top_element(self):
        if self.head == None:
            print("Stack is empty")
            return False
        return self.head.data

    def peek_at_bottom_element(self):
        if self.head == None:
            print("Stack is empty")
            return False
        itr = self.head
        for _ in range(self.size - 1):
            itr = itr.reference_of_next_node
        return itr.data

    def peek_at_the_middle_with_index_number(self, index):
        if self.head == None:
            print("Stack is empty")
            return False
        itr = self.head
        for i in range(index - 1):
            itr = itr.reference_of_next_node
        return itr.data

    def peek_at_the_middle_with_reference_of_values(self, data):
        if self.head == None:
            print("Stack is empty")
            return False
        itr = self.head
        while data != itr.data:
            itr = itr.reference_of_next_node
        return itr.data

    def delete_top_element(self):
        if self.head == None:
            print("Stack is empty")
            return False
        self.size -= 1
        temp = self.head.data
        self.head = self.head.reference_of_next_node
        return temp

    def delete_bottom_element(self):
        if self.head == None:
            print("Stack is empty")
            return False
        itr = self.head
        for i in range(self.size - 2):
            itr = itr.reference_of_next_node
        temp = itr.reference_of_next_node.data
        itr.reference_of_next_node = None
        self.size -= 1
        return temp

    def delete_element_in_the_middle_with_index_number(self, index):
        itr = self.head
        pre = itr
        if self.head == None:
            print("Stack is empty")
            return False
        if index == 0:
            temp = self.head.data
            self.head = self.head.reference_of_next_node
            return temp
        for i in range(index):
            pre = itr
            itr = itr.reference_of_next_node
        temp = itr.data
        pre.reference_of_next_node = itr.reference_of_next_node
        self.size -= 1
        return temp

    def delete_element_in_the_middle_with_reference_of_values(self, data):
        itr = self.head
        previous = itr
        if self.head == None:
            print("Stack is empty")
            return False
        self.size -= 1
        while data != itr.data:
            previous = itr
            itr = itr.reference_of_next_node
        temp = itr.data
        previous.reference_of_next_node = itr.reference_of_next_node
        return temp

    def print_all(self):
        itr = self.head
        for i in range(self.size):
            print(i, itr, itr.data, itr.reference_of_next_node)
            itr = itr.reference_of_next_node

    def print_again(self):
        itr = self.head
        i = 0
        while itr.reference_of_next_node != None:
            print(i, itr, itr.data, itr.reference_of_next_node)
            i += 1
            itr = itr.reference_of_next_node
        print("  ", i, itr, itr.data, itr.reference_of_next_node)


if __name__ == "__main__":
    link_list = Linked_List()
    link_list.insert_at_the_beginning(89)
    link_list.insert_at_the_beginning(895)
    link_list.insert_at_the_beginning(869)
    link_list.insert_at_the_beginning(489)
    link_list.insert_at_the_beginning(889)
    link_list.insert_at_the_beginning(189)
    link_list.insert_at_the_beginning(789)
    link_list.insert_at_the_end(12)
    link_list.insert_at_the_end(34)
    link_list.insert_at_the_end(65)
    link_list.insert_at_the_end(68)
    link_list.insert_at_the_end(578)
    link_list.insert_at_the_end(15)
    link_list.insert_at_the_end(547)
    link_list.insert_at_the_end(346)
    link_list.insert_at_the_end(468)
    link_list.insert_at_the_end(26)
    link_list.insert_at_the_end(98)
    link_list.insert_at_the_end(1254)
    link_list.insert_at_the_end(2465)
    link_list.insert_at_the_end(151)
    link_list.insert_at_the_end(1111)
    link_list.insert_in_the_middle(2, 455)
    link_list.insert_in_the_middle(5, 6658)
    link_list.insert_in_the_middle(3, 464)
    link_list.insert_in_the_middle(7, 676)
    link_list.insert_in_the_middle(8, 574)
    link_list.print_all()
    link_list.delete_bottom_element()
    link_list.delete_bottom_element()
    link_list.delete_bottom_element()
    link_list.delete_bottom_element()
    link_list.delete_top_element()
    link_list.delete_top_element()
    link_list.delete_top_element()
    link_list.delete_top_element()
    link_list.print_all()
    print("  ")
    link_list.print_again()
    print(link_list.peek_the_top_element())
    print(link_list.peek_at_bottom_element())
    print(link_list.peek_at_the_middle_with_index_number(6))
    link_list.delete_element_in_the_middle_with_index_number(4)
    link_list.delete_element_in_the_middle_with_index_number(0)
    link_list.delete_element_in_the_middle_with_index_number(1)
    print("length of list is :", link_list.length())
