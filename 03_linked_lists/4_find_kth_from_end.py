class Node :  	 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value, nextNode = None):
        self.data = value
        self.next = nextNode

# Find the kth node from the end, Time O(n), Space O(1)
def find_kth_from_end(head, k):
    fast = head
    slow = head    
    for i in range(0, k):
        if fast == None: # special case k > n
            print("invalid input.")
            return None 
        fast = fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow

# Find the middle node in the list, Time O(n), Space O(1)
def find_middle(head):
    if head == None:
        return
    slow = head
    fast = head        
    while  fast.next != None and fast.next.next != None:             
        slow = slow.next
        fast = fast.next.next
    return slow

# Print list, Time O(n), Space O(1) 
def display(head):
    p = head
    while p != None:
        print(p.data, end=' ')
        p = p.next
    print()

# test
# insert list into a linked list 
list = [4, 6, 2, -9, 0, 3]
head = None
for i in reversed(list):
    head = Node(i, head)
display(head)

key = 3
node = find_kth_from_end(head, key)
if node != None:
    print("find "+ str(key)+ "th from end: " + str(node.data))

node = find_middle(head)
print("find middle: "+ str(node.data))