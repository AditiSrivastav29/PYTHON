class Node:
    def _init_(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def _init_(self):
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
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(4)
linked_list.insert(1)

linked_list.sort()
linked_list.print_list()