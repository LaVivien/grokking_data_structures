# Write a function to insert a node in a sorted list.

class Node:  	 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value, nextNode = None):
        self.data = value
        self.next = nextNode

# Insert in a sorted list, Time O(n), Space O(1) 
def insert_sorted_list(head, key):
    newNode = Node(key)
    if head == None:
        head = newNode
    if key > head.data:           
        curr = head                                          
        while curr.next != None and key > curr.next.data:
            curr = curr.next                       
        newNode.next = curr.next      
        curr.next = newNode
    else:
        newNode.next = head      
        head = newNode
    return head # head might be changed

# Print list, Time O(n), Space O(1)   
def display(head):
    p = head
    while p != None:
        print(p.data, end = ' ')
        p = p.next
    print()

# test
# insert 4 in the list
head = Node(4)
head = insert_sorted_list(head, -23)
head = insert_sorted_list(head, 6)
head = insert_sorted_list(head, 9)
display(head)

