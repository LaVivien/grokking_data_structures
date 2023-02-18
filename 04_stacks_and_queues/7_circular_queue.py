class CircularQueue:

    # Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.max_size = size
        self.queue = [None] * size
        self.front_index = self.rear_index = -1
        self.queue_size = 0

    # Add at the rear, Time O(1), Space O(1)
    def enqueue(self, value):
        if self.is_full(): # full
            print("The circular queue is full, cannot enqueue")
            return
        if self.is_empty(): # empty
            self.front_index = 0
        self.rear_index = (self.rear_index + 1) % self.max_size
        self.queue[self.rear_index] = value
        self.queue_size += 1

    # Remove from the front, Time O(1), Space O(1)
    def dequeue(self):
        if self.is_empty(): # edge case, empty
            print("The circular queue is empty, cannot dequeue")
            return None
        item = self.queue[self.front_index]
        if (self.front_index == self.rear_index): #edge case, dequeue last item
            self.front_index = -1
            self.rear_index = -1
        else:           
            self.front_index = (self.front_index + 1) % self.max_size
        self.queue_size -= 1
        return item

    # Return the front value, Time O(1), Space O(1)
    def peek(self):
        if self.is_empty():
            print("The circular queue is empty, cannot peek")
            return None
        return self.queue[self.front_index]

    # Print all, Time O(n), Space O(1), n is number of items in queue
    def print(self):
        if self.is_empty():
            print("The circular queue is empty")
            return
        print("Circular queue: ", end="")
        i = self.front_index   
        while i != self.rear_index:
            print(str(self.queue[i]) , end=" ")
            i = (i + 1) % self.max_size
        print(self.queue[i])      
        
	# Return number of items in queue, Time O(1), Space O(1)
    def size(self):
        return self.queue_size

    # Check full, Time O(1), Space O(1)
    def is_full(self):
        return (self.rear_index + 1) % self.max_size == self.front_index

    # Check empty, Time O(1), Space O(1)
    def is_empty(self):
        return self.front_index == -1

# Test
if __name__ == '__main__':
    #Initialize, enqueue, size
    queue = CircularQueue(5); 
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
    print("\ndequeue")
    queue.dequeue()  
    queue.dequeue()  
    queue.print() 
    print("size: " + str(queue.size())) 
    print("peek: " + str(queue.peek())) 

    #Enqueue again
    print("\nenqueue again")
    queue.enqueue(60)
    queue.enqueue(33)
    queue.enqueue(22)
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))   

    print("is empty: " + str(queue.is_empty()))
    print("is full: " + str(queue.is_full()))
 
