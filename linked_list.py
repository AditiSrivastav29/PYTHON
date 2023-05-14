class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

linked_list = LinkedList()

while True:
    element = input("Enter an element of the linked list (or enter 'q' to stop): ")
    if element == 'q':
        break
    linked_list.append(int(element))

linked_list.print_list()

