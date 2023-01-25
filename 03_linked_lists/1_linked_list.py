class Node:  
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value):
        self.data = value
        self.next = None	
	
    # Time O(1), Space O(1)
    def __str__(self):
	    return str(self.data)
	
class LinkedList :
    # Constructor, Time O(1), Space O(1)
    def __init__ (self):
        self.head = None

    # Add at the head, Time O(1), Space O(1)
    def insert_first(self, value):                         
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    # Add at the end, Time O(n), Space O(1), n is number of nodes in list
    def insert_last(self, value):
        newNode = Node(value)
        if self.head == None: # edge case, first node
            self.head = newNode
            return        
        curr = self.head     
        while curr.next != None:
            curr = curr.next
        curr.next = newNode

    # Insert after the node, Time O(1), Space O(1)
    def insert_after(self, curr, value): 
        if curr is None:
            print("The input node in None.")
            return
        newNode = Node(value)
        newNode.next = curr.next
        curr.next = newNode

    # Delete the first node, Time O(1), Space O(1)
    def delete_first(self) :  
        if self.head == None:   #empty list 
            return  
        self.head = self.head.next 

    # Delete the first found node by key, Time O(n), Space O(1)
    def delete(self, key) :
        curr = self.head 
        if self.head == None: #edge case, empty
            return 
        elif  self.head.data == key: #edge case, head is key
            self.head = self.head.next
            return
        prev = None  
        while curr != None:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    # Delete all notes by key, Time O(n), Space O(1)
    def delete_all_keys(self, key): 
        curr = self.head
        prev = None  
        while curr != None:
            if curr.data == key:
                if prev == None: #edge case, first node
                    self.head = curr.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next

    # Search by key, return the first found item, Time O(n), Space O(1)
    def search(self, key):
        curr = self.head
        while curr != None:
            if curr.data == key:
                return curr
            curr = curr.next
        return None
    
    # Print the list, Time O(n), Space O(1)
    def traverse(self):
        curr = self.head
        while curr != None:
            print(str(curr.data), end = ' ')
            curr = curr.next
        print()

# test
if __name__ == '__main__':
    # Initialize, insert, print 
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_last(64)
    ll.insert_last(32)
    ll.insert_last(11)
    ll.insert_last(3)
    ll.insert_last(19)
    ll.insert_last(32)
    ll.insert_first(-5)
    ll.traverse()

    ll.delete_first()
    ll.traverse()

    # Delete by key
    key = 3
    print("delete by key " + str(key))
    ll.delete(key)
    ll.traverse()

    # Search
    key = 11
    node = ll.search(key)
    print("find value: "+ str(node))

    # Insert after
    ll.insert_after(node, -99)
    ll.traverse()

    # Delete all matched keys
    ll.delete_all_keys(32)
    ll.traverse()
