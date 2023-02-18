class Node:
    # Constructor, Time O(1), Space O(1)
    def __init__(self, value):
        self.data = value
        self.next = None

    # Override the print format, Time O(1), Space O(1)
    def __str__(self):
        return str(self.data)

class Queue:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.front = self.rear = None
        self.queue_size = 0
     
    # Add at the rear, Time O(1), Space O(1)
    def enqueue(self, value):
        new_node = Node(value)        
        if self.is_empty():
            self.front = self.rear = new_node
        else: 
            self.rear.next = new_node
            self.rear = new_node
        self.queue_size +=1
 
    # Remove from the front, Time O(1), Space O(1)
    def dequeue(self):        
        if self.is_empty(): #edge case, empty list
            print("Queue is empty, cannot dequeue")
            return None
        front_item = self.front
        self.front = self.front.next
        self.queue_size -= 1
        if (self.front == None):  # edge case, deleted last one, now empty
            self.rear = None
        return front_item

    # Return the front node , Time O(1), Space O(1)
    def peek(self) :
        if self.is_empty():
            print("Queue is empty, cannot peek")
            return None
        return self.front

    # Print all, Time O(n), Space O(1), n is number of items in queue
    def print(self) :
        curr = self.front
        while curr != None:
            print(str(curr.data), end = ' ')
            curr = curr.next
        print()

    # Return number of nodes, Time O(1), Space O(1)
    def size(self) :
        return self.queue_size

    #Check empty, Time O(1), Space O(1)
    def is_empty(self):
        return self.front == None

# test
if __name__ == '__main__':
#Initialize, enqueue, size
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(80)        
    queue.enqueue(54)
    queue.enqueue(60)		
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))

    #Dequeue
    print("\ndequeue:")
    a = queue.dequeue()
    print(a) 
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))

    #enqueue again
    print("\nenqueue again:")
    queue.enqueue(70)
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))

