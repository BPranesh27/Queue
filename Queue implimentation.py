class queue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.size = size
        self.queue_list = [None] * size

    def isfull(self):
        return self.rear == self.size - 1

    def isEmpty(self):
        return self.front is None or self.front > self.rear

    def Enqueue(self, val):
        if self.isfull():
            print("QUEUE is full")
        else:
            if self.front is None:
                self.front = 0
                self.rear = 0
            else:
                self.rear += 1
            self.queue_list[self.rear] = val

    def Dequeue(self):
        if self.isEmpty():
            print("QUEUE has no Element")
        else:
            rem = self.queue_list[self.front]
            self.queue_list[self.front] = None
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front += 1
            return rem

    def peak(self):
        if self.isEmpty():
            print("QUEUE has no Element")
        else:
            return self.queue_list[self.front]

# Usage
que = queue(int(input("Enter the size of queue: ")))
print("1-Enqueue, 2-Dequeue, 3-Peak, 4-Empty, 5-Full, 6-Exit")

while True:
    cas = int(input())

    match cas:
        case 1:
            que.Enqueue(int(input("Enter the enqueue element: ")))
            print(que.queue_list)
        case 2:
            print("Dequeued Element:", que.Dequeue())
            print(que.queue_list)
        case 3:
            print("Peak of Queue:", que.peak())
        case 4:
            print("Queue is Empty:", que.isEmpty())
        case 5:
            print("Queue is Full:", que.isfull())
        case 6:
            break
