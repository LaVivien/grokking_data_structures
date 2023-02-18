class Node:
    #Constructor, Time O(1), Space O(1)
    def __init__(self, value):
        self.data = value
        self.next = None
        self.pre = None

class Deque:
    #Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.front = self.rear = None
        self.deque_size = 0    
    
    # Add at the head, Time O(1), Space O(1) 
    def insert_first(self, value):
        new_node = Node(value)
        if self.front == None: # edge case
            self.rear = new_node
        else:
            self.front.pre = new_node
            new_node.next = self.front
        self.front = new_node
        self.deque_size += 1

    # Add at the tail, Time O(1), Space O(1) 
    def insert_last(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
        else:
            self.rear.next = new_node
            new_node.pre = self.rear
        self.rear = new_node                     
        self.deque_size += 1

    # Delete the first node, Time O(1), Space O(1)
    def delete_first(self):  
        if self.front == None:   #empty list 
            return  
        if self.front != self.rear:  # at least two nodes
            self.front = self.front.next 
            self.front.pre = None 
        else :
            self.front = self.rear = None #edge case, last node
        self.deque_size -= 1

    # Delete the last node, Time O(1), Space O(1)
    def delete_last(self):  
        if self.front == None:  #empty list 
             return   
        if self.front != self.rear: # at least two nodes
            self.rear =  self.rear.pre 
            self.rear.next = None  
        else :
           self.front = self.rear = None #edge case, last node
        self.deque_size -= 1

    #Return front value, Time O(1), Space O(1)
    def get_first(self) :
        if self.is_empty():
            return None
        return self.front.data

    #Return last value, Time O(1), Space O(1)
    def get_last(self) :
        if self.is_empty():
            return None
        return self.rear.data   

    #Print all, Time O(n), Space O(1), n is number of items in queue
    def print(self) :
        node = self.front
        while node != None:
            print(str(node.data), end= " ")
            node = node.next
        print()

    #Return length, Time O(1), Space O(1)
    def size(self) :
        return self.deque_size

    #Check empty, Time O(1), Space O(1)
    def is_empty(self):
        return self.front == None

# Test
if __name__ == '__main__':
    #Initialize, enqueue, size
    deque = Deque()
    deque.insert_first(4)
    deque.insert_last(64)
    deque.insert_last(-6)
    deque.insert_last(3)
    deque.insert_last(32)
    deque.insert_last(-6)
    deque.insert_last(11)
    deque.insert_first(19)	
    deque.print()
    print("size: " + str(deque.size()))
    print("first: " + str(deque.get_first()))
    print("last: " + str(deque.get_last()))

    #Dequeue
    deque.delete_first() 
    deque.delete_last()
    deque.print()
    print("size: " + str(deque.size()))
    print("first " + str(deque.get_first()))
    print("last: " + str(deque.get_last()))

    #enqueue again
    deque.insert_last(70)
    deque.print()
    print("size: " + str(deque.size()))
    print("first: " + str(deque.get_first()))
    print("last: " + str(deque.get_last()))