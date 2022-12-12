class DllNode: 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value): 
        self.data = value
        self.next = None
        self.pre = None
	
	# Time O(1), Space O(1)
    def __str__(self):
	    return str(self.data)

class DoublyLinkedList:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Add at the head, Time O(1), Space O(1) 
    def insert_first(self, value):
        newNode = DllNode(value)
        if self.head == None: # edge case
            self.tail = newNode
        else:
            self.head.pre = newNode
            newNode.next = self.head
        self.head = newNode

    # Add at the tail, Time O(1), Space O(1) 
    def insert_last(self, value):
        newNode = DllNode(value)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.pre = self.tail
        self.tail = newNode
        
    # Insert after the node, Time O(n), Space O(1)
    def insert_after (self, curr, value):                              
        if curr == None:          
            return
        newNode = DllNode(value)        
        if curr == self.tail:
            newNode.next = None        
            self.tail = newNode             
        else:
            newNode.next = curr.next
            curr.next.pre = newNode
        newNode.pre = curr    
        curr.next = newNode                 
    
    # Delete the first node, Time O(1), Space O(1)
    def delete_first(self):  
        if self.head == None:   #empty list 
            return  
        if self.head != self.tail:  # at least two nodes
            self.head = self.head.next 
            self.head.pre = None 
        else :
            self.head = self.tail = None #edge case, last node

    # Delete the last node, Time O(1), Space O(1)
    def delete_last(self):  
        if self.head == None:  #empty list 
             return   
        if self.head != self.tail: # at least two nodes
            self.tail =  self.tail.pre 
            self.tail.next = None  
        else :
           self.head = self.tail = None #edge case, last node

    # Delete the first found item, Time O(n), Space O(1)
    def delete(self, key):   
        if self.head == None:
            return                           
        curr = self.head          
        while curr.data != key:
            curr = curr.next     
            if curr == None:
                return          
        if curr == self.head:    # edge case, the node is head      
            self.head = curr.next       
        else:                       
            curr.pre.next = curr.next        
        if curr == self.tail:         # edge case, the node is tail  
            self.tail = curr.pre    
        else:                         
            curr.next.pre = curr.pre

    # Delete all nodes with key, Time O(n), Space O(1)
    def delete_all_keys(self, key):
        if self.head == None: 
            return None 
        curr = self.head 
        next = None 
        while curr != None: 
            if curr.data == key: 
                next = curr.next 
                self.delete_node(curr)
                curr = next              
            else:
                curr = curr.next 
        return self.head  
    
    # Delete a node, Time O(1), Space O(1)
    def delete_node(self, curr):
        if curr == None:
            return
        if curr.pre != None:
            curr.pre.next = curr.next
        else:
            self.head = curr.next    # edge case           
        if curr.next != None:
            curr.next.pre = curr.pre
        else:
            self.tail = curr.pre # edge case  

	# Search by key, return the first found item, Time O(n), Space O(1) 
    def search(self, key):
        curr = self.head   
        while curr != None: 
            if curr.data == key:
                return curr 
            curr = curr.next  
        return None    
	
	# Print both directions, Time O(n), Space O(1) 
    def display(self):
        if self.head == None:
            print ("The list is empty")
            return
        print("first-->last: ", end = '')
        curr = self.head        
        while curr != None:
            print(str(curr.data), end = ' ')
            curr = curr.next   
        print()
        
        print("last-->first: ", end = '')
        curr = self.tail         
        while curr != None:
            print(str(curr.data), end = ' ')
            curr = curr.pre
        print()
            
#Initialize, insert and print 
dll = DoublyLinkedList()
dll.insert_first(4)
dll.insert_last(64)
dll.insert_last(-6)
dll.insert_last(3)
dll.insert_last(32)
dll.insert_last(-6)
dll.insert_last(11)
dll.insert_first(19)
dll.display();            

print("delete first and last")                 
dll.delete_first()
dll.delete_last()
dll.display()

#add first and last again
dll.insert_first(51)
dll.insert_last(-6)
dll.display()

#search and delete
key = -6
node = dll.search(key)
print("Search " + str(key) + " :" + str(node))

dll.delete_all_keys(key)
print("Delete " + str(key) + " :" + str(node))
dll.display()

#insert after
print("insert after")   
key = 4
node = dll.search(key)
dll.insert_after(node, 5)
dll.display()

#delete by key
dll.delete(key)
print("Delete node:" + str(node))
dll.display()
