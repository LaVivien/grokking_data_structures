# Write a function to detect whether there is a loop in a linked list.
	
class Node :  	 
    # Constructor, Time O(1), Space O(1)
    def __init__(self, value, nextNode = None):
        self.data = value
        self.next = nextNode	

# Detect loop, Two pointers, Time O(n), Space O(1), n is number of nodes in list
def detect_loop(head) :
    if head == None:
        return False		
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# test 
# creat a list, the last node is head 
n5 = Node(10)
n4 = Node(-1, n5)
n3 = Node(7, n4)
n2 = Node(2, n3)
n1 = Node(8, n2)
print("before add loop: "+ str(detect_loop(n1)))

n3.next = n1 # form a loop
print("after add loop: "+ str(detect_loop(n1)))