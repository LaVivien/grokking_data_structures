my_stack = __import__('1_stack')

class Queue:
    # Constructor, queue has limited size, Time O(1), Space O(n)
    def __init__(self, size):
        self.stack = my_stack.Stack(size)
        self.queue_size = size
	
	# Add at the rear, Time O(m), Space O(n), m is number of items in stack, n is intial size
    def enqueue(self, value) :
        tmp_stack = my_stack.Stack(self.queue_size)
        while not self.stack.is_empty(): 
            tmp_stack.push(self.stack.pop())
        self.stack.push(value)
        while not tmp_stack.is_empty(): 
            self.stack.push(tmp_stack.pop())
	
	# Remove from the front, Time O(1), Space O(1)
    def dequeue(self) :
        return self.stack.pop()

	#Return the front value, Time O(1), Space O(1)
    def peek(self):
        return self.stack.top()

	#Return queue size, Time O(1), Space O(1)
    def size(self) :
        return self.stack.size()
	
	# Check empty, Time O(1), Space O(1)
    def is_empty(self) :
        return self.stack.is_empty()

    # Check full, Time O(1), Space O(1)
    def is_full(self) :
        return self.stack.is_full()

    # print all, Time O(n), Space O(1)
    def print(self):
        self.stack.print()

#Initialize, enqueue, size
if __name__ == '__main__':
    queue = Queue(5)
    queue.enqueue(18)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(80)        
    queue.enqueue(54)
    queue.enqueue(60)		
    queue.print()
    print("size:" + str(queue.size()))
    print("peek:" + str(queue.peek()))

    # #Dequeue
    queue.dequeue() 
    queue.dequeue()
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))

    # #enqueue again
    queue.enqueue(70)
    queue.print()
    print("size: " + str(queue.size()))
    print("peek: " + str(queue.peek()))
    print("is empty: " + str(queue.is_empty()))
    print("is full: " + str(queue.is_full()))