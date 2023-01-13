"""
Write a Menu-Driven OOP Program to build and Manage a QUEUE.Use the List data type in python.The User Should
be able to perform various operations on the QUEUE, such as:
1. ENQUEUE an element to the QUEUE.
2. DEQUEUE an element from the QUEUE.
3. COUNT the number of elements in the QUEUE.
4. DISPLAY ALL the elements in the QUEUE.
5. CONVERT the QUEUE to a PRIORITY QUEUE.
"""
class QUEUE:
    def __init__(self):
        self.__list = []

    def count(self):
        return len(self.__list)

    def enqueue(self, item):
        self.__list.append(item)
        return f"{item} is Enqueued!"

    def dequeue(self):
        item = self.__list[0]
        self.__list.pop(0)
        return f"{item} DEQUEUED!"

    def displayAll(self):
        print("THIS IS THE DISPLAY FUNCTION!")
        print(f"The Current QUEUE IS: {self.__list}")

    def toPriorityQueue(self):
        priority_queue = self.__list
        for i in range(0,len(priority_queue)):
            for j in range(i+1,len(priority_queue)):
                if priority_queue[i] > priority_queue[j]:
                    temp = priority_queue[i]
                    priority_queue[i] = priority_queue[j]
                    priority_queue[j] = temp
        return print(f"Priorities are SET successfully as {priority_queue}")

#Driver Code
S1 = QUEUE()
while True:
    print("----------------------------MENU----------------------------")
    operation = int(input('''What is the Operation you want to perform? 
    1. ENQUEUE
    2. DEQUEUE
    3. COUNT
    4. DISPLAY ALL
    5. CONVERT TO PRIORITY QUEUE
    6. Exit - '''))

    if operation == 1:
        push_item = int(input("Enter the Element you want to Enqueue: "))
        push = S1.enqueue(push_item)
        print(push)
    elif operation == 2:
        pop = S1.dequeue()
        print(pop)
    elif operation == 3:
        num_items = S1.count()
        print(f"The Number of Items in the QUEUE are: {num_items}")
        continue
    elif operation == 4:
        S1.displayAll()
    elif operation == 5:
        S1.toPriorityQueue()
    elif operation == 6:
        break
    else:
        print("Invalid Option!")
        continue