"""
Write a Menu-Driven OOP Program to build and Manage a STACK.Use the List data type in python.The User Should
be able to perform various operations on the STACK, such as:
1. PUSH an element to the STACK.
2. POP an element from the STACK.
3. COUNT the number of elements in the STACK.
4. DISPLAY ALL the elements in the STACK.
5. DISPLAY TOPMOST element of the STACK.
"""

class STACK:
    def __init__(self):
         self.__index = []

    def __len__(self):
        return len(self.__index)

    def push(self, item):
        self.__index.append(item)
        return f"{item} PUSHED!"

    def pop(self):
        if len(self) == 0:
            raise Exception("pop() called on Empty Stack.")
        else:
            self.__index.pop(-1)
            return "ELEMENT POPPED!"
    def displayAll(self):
        print("THIS IS THE DISPLAY FUNCTION!")
        print(f"The Current STACK IS: {self.__index}")

    def peek(self):
        if len(self) == 0:
            raise Exception("peek() called on Empty Stack.")
        else:
            return print(f"The Topmost Element is: {self.__index[-1]}")

#Driver Code
S1 = STACK()
while True:
    print("----------------------------MENU----------------------------")
    operation = int(input('''What is the Operation you want to perform? 
    1. PUSH
    2. POP
    3. COUNT
    4. DISPLAY ALL
    5. DISPLAY TOP
    6. Exit - '''))

    if operation == 1:
        push_item = int(input("Enter the Element you want to push: "))
        push = S1.push(push_item)
        print(push)
        continue
    elif operation == 2:
        pop = S1.pop()
        print(pop)
        continue
    elif operation == 3:
        num_items = S1.__len__()
        print(f"The Number of Items in the STACK are: {num_items}")
        continue
    elif operation == 4:
        S1.displayAll()
        continue
    elif operation == 5:
        S1.peek()
        continue
    elif operation == 6:
        break
    else:
        print("Invalid Option!")
        continue