class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head              #curr = self.head       So, here curr denotes last_node
            while last_node.next:              #while curr.next
                last_node = last_node.next     # curr = curr.next
            last_node.next = new_node          # curr.next = new_node

    def delete_at_beginning(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node = None
        else:
            print(" list is empty ")

    
    def delete(self, X):              # Here temp = current_node
        temp = self.head                # X = value to be deleted
        if temp and temp.data == X:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp:
            if temp.data == X:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None


    def search(self, key):
        current_node = self.head
        prev = None
        index = 0
        while current_node:
            if current_node.data == key:
                print("Found at index:", index)
                return
            prev = current_node
            current_node = current_node.next
            index += 1
        print("Not found in the linked list")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.insert_at_beginning(0)
    linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.delete_at_beginning()
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.delete(3)
    linked_list.print_list()  # Output: 1 -> 2 -> 4 -> 5 -> None

    print(linked_list.search(3))  # Output: False
    print(linked_list.search(4))  # Output: True
