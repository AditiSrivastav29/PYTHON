stack = []
top = -1

def push():
    if top == n - 1:
        print("Overflow")
    else:
        val = int(input("Enter the value: "))
        stack.append(val)
        globals()['top'] += 1

def pop():
    if top == -1:
        print("Underflow")
    else:
        stack.pop()
        globals()['top'] -= 1

def show():
    if top == -1:
        print("Stack is empty")
    else:
        for i in range(top, -1,-1):
            print(stack[i])

def main():
    global n
    n = int(input("Enter the size of the stack: ")) #no.of elements in the stack
   
    choice = 0
    while choice != 4:
        print("Choose one from the below options...")
        print("1. Push")
        print("2. Pop")
        print("3. Show")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            show()
        elif choice == 4:
            print("Exiting....")
        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()
