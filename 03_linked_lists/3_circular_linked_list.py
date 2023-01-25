
class Node :  	 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value):
        self.data = value
        self.next = None	
	
    # Time O(1), Space O(1)
    def __str__(self):
	    return str(self.data)
	
class CircularLinkedList:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.head = None
        self.last = None # the last inserted node

    # Insert at last insertion position, Time O(1), Space O(1)
    def insert_last(self, value):                         
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else: 
            self.last.next = newNode
        self.last = newNode
        self.last.next = self.head

    # Insert node after a specific key, Time O(n), Space O(1)
    def insert_after(self, key, value):
        newNode = Node(value)
        curr = self.head
        while curr:
            if curr.data == key:
                newNode.next = curr.next
                curr.next = newNode
                if curr == self.last: #edge case, insert after last
                    self.last = newNode
                return self.last
            curr = curr.next           
            if curr == self.head: # reaches head, key is not found
                print("cannot find " + str(key) +", stop insert.")
                break

    # Delete the first found item, Time O(n), Space O(1)
    def delete(self, key):
        node = self.search(key)
        if node == None:
            print("not found "+ str(key))
            return
        prev = self.head
        curr = self.head.next
        while curr.data != key:
            prev = curr
            curr = curr.next      
        if self.head == self.last: #only one left
            print ("delete last")
            self.head = None
        elif curr == self.head:  #delete head itself
            prev.next = curr.next
            self.head = curr.next
        else:
            prev.next = curr.next
    
    # Search by key, return the first found item, Time O(n), Space O(1)
    def search(self, key):
        if self.head == None: 
            print("empty list")
            return None
        curr = self.head
        while True:
            if curr.data == key:
                return curr
            curr = curr.next
            if curr == self.head:
                break
        return None
    
    # Print the list, Time O(n), Space O(1)
    def print(self):
        if self.head == None: 
            print("empty list")
            return
        curr = self.head
        while True:
            print(str(curr.data), end = ' ')
            curr = curr.next
            if curr == self.head:
                break
        print()

# test
if __name__ == '__main__':
    #Initialize and insert
    cll = CircularLinkedList()
    cll.insert_last(3)
    cll.insert_last(64)
    cll.insert_last(32)
    cll.insert_last(19)
    cll.insert_last(-5)
    cll.print()

    cll.insert_after(19, 33)
    cll.print()

    # search and Delete by key
    key = 32
    node = cll.search(key)
    print("found "+ str(key) + ": " + str(node))

    cll.delete(key)
    cll.print()
