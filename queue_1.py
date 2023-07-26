maxsize = 5
queue = []

def insert():
    item = int(input("Enter the element: "))
    if len(queue) == maxsize:
        print("Overflow")
    else:
        queue.append(item)
        print("Value inserted")

def delete():
    if len(queue) == 0:
        print("Underflow")
    else:
        item = queue.pop(0)
        print("Value deleted")

def display():
    if len(queue) == 0:
        print("Empty queue")
    else:
        print("Printing values...")
        for item in queue:
            print(item)

def main():
    while True:
        
        print("\n1. Insert an element")
        print("2. Delete an element")
        print("3. Display the queue")
        print("4. Exit")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            insert()
        elif choice == 2:
            delete()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("\nEnter valid choice")

if __name__ == "__main__":
    main()
