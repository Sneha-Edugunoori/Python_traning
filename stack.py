class Stack:
    def __init__(self):
        self.ListStack = []  # List represents the stack
    
    def push(self, data):
        self.ListStack.append(data)  # Push operation appends data to the end of the list
    
    def pop(self):
        if len(self.ListStack) == 0:
            print("Stack is empty. Cannot perform pop operation.")
        else:
            return self.ListStack.pop()  # Pop operation removes and returns the last element from the list
    
    def display(self):
        print("Stack =", self.ListStack)

    def peek(self):
        return self.ListStack[-1]  # Returns the top element of the stack without removing it

    def delete(self):
        del self.ListStack[:]  # Deletes all elements from the stack

if __name__ == '__main__':
    obj = Stack()  # Object created for Stack
    
    while True:
        print("\n**********Stack Operations**********")
        print("1. Push operation")
        print("2. Pop operation")
        print("3. Display stack")
        print("4. Peek operation")
        print("5. Delete stack")
        print("6. Exit")
        print("===============================")
        ch = int(input("Enter your choice: ")) 
        print("===============================")
        if ch == 1:
            item = int(input("Enter the element to push: "))
            obj.push(item)
            print("**Push operation performed.**")
        elif ch == 2:
            popped = obj.pop()
            if popped is not None:
                print(f"**Popped element:** {popped}")
        elif ch == 3:
            obj.display()
        elif ch == 4:
            print(obj.peek())  
        elif ch == 5:
            obj.delete()
        elif ch == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")