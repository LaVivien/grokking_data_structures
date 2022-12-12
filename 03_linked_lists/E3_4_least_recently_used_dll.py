# Write a class of doubly linked list with the LRU capability. 

class DllNode: 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value): 
        self.data = value
        self.next = None
        self.pre = None

class LeastRecentlyUsedDll:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.head = None
        self.tail = None

    # Public API, Add an item, Time O(n), Space O(1)
    def put(self, key):
        node = self.search(key)
        if node == None:
            newNode = DllNode(key)
            self.addNode(newNode) # insert at head
        else:
            self.removeNode(node)
            self.addNode(node) # move to head
          
    # Public API, Query an item, Time O(n), Space O(1)
    def get(self, key):
        node = self.search(key)
        if node == None:
            return
        self.removeNode(node)
        self.addNode(node); # move to head

    # Private method, Search by key, Time O(n), Space O(1) 
    def search(self, key):
        if self.head == None:
            return None
        curr = self.head   
        while curr != None: 
            if curr.data == key:
                return curr 
            curr = curr.next  
        return None        

    # Private method, Add a node, Time O(1), Space O(1)
    def addNode(self, node):
        if self.head != None:
            self.head.pre = node # always add at head
        node.next = self.head
        node.pre = None
        self.head = node
        if self.tail == None: 
            self.tail = self.head

    # Private method, Remove a node, Time O(1), Space O(1)
    def removeNode(self, node):
        if node.pre != None: 
            node.pre.next = node.next
        else: 
            self.head = node.next    #edge case, move head to next   
        if node.next != None:
            node.next.pre = node.pre
        else:
            self.tail = node.pre  #edge case, move tail to pre

    # Print the list, Time O(n), Space O(1)
    def display(self):
        p = self.head
        while p != None:
            print(p.data, end = ' ')
            p = p.next
        print()

# creat a list
dll = LeastRecentlyUsedDll()
dll.put(-1)
dll.put(6)
dll.put(2)
dll.put(14)
dll.put(7)
dll.put(3)
dll.display()

dll.put(7)
dll.display()

dll.put(3)
dll.display()

dll.put(6)
dll.display()

dll.put(5)
dll.display()

dll.get(7)
dll.display()