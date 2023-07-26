class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def sort(self):
        current = self.head
        if current is None:
            return
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                current = self.head
            else:
                current = current.next

    def print_list(self):
        current = self.head
        while current:                                                                      
            print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.insert(int(input()))
linked_list.insert(int(input()))
linked_list.insert(int(input()))
linked_list.insert(int(input()))
linked_list.insert(int(input()))

linked_list.sort()
linked_list.print_list()
