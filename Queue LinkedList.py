class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.size = size
        self.current_size = 0

    def isfull(self):
        return self.current_size == self.size

    def isEmpty(self):
        return self.front is None

    def Enqueue(self, val):
        if self.isfull():
            print("QUEUE is full")
        else:
            new_node = Node(val)
            if self.rear is None:
                # Queue is empty
                self.front = self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node
            self.current_size += 1

    def Dequeue(self):
        if self.isEmpty():
            print("QUEUE has no Element")
        else:
            removed_value = self.front.value
            self.front = self.front.next
            if self.front is None:
                # If the queue becomes empty after the dequeue
                self.rear = None
            self.current_size -= 1
            return removed_value

    def peak(self):
        if self.isEmpty():
            print("QUEUE has no Element")
        else:
            return self.front.value

    def display(self):
        if self.isEmpty():
            print("QUEUE is empty")
        else:
            temp = self.front
            queue_elements = []
            while temp:
                queue_elements.append(temp.value)
                temp = temp.next
            print("Queue:", queue_elements)

# Usage
que = Queue(int(input("Enter the size of queue: ")))
print("1-Enqueue, 2-Dequeue, 3-Peak, 4-Empty, 5-Full, 6-Exit")

while True:
    cas = int(input())

    match cas:
        case 1:
            que.Enqueue(int(input("Enter the enqueue element: ")))
            que.display()
        
        case 2:
            print("Dequeued Element:", que.Dequeue())
            que.display()

        case 3:
            print("Peak of Queue:", que.peak())

        case 4:
            print("Queue is Empty:", que.isEmpty())

        case 5:
            print("Queue is Full:", que.isfull())

        case 6:
            break

        case _:
            print("Invalid operation. Please try again.")
