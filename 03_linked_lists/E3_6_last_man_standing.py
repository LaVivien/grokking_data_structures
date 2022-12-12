# Write a function to solve Josephus problem with a circular linked list.

class LinkNode :  	
    # Constructor, Time O(1), Space O(1)
    def __init__(self, value):
        self.data = value
        self.next = None

# Create circular linked list,  Time O(n), Space O(n), n is input number
def last_man_standing(n, m):
    head = LinkNode(1)  # the frist node is 1
    prev = head
    for i in range(2, n+1):  # contiue to build circular linked list 
        prev.next = LinkNode(i); 
        prev = prev.next
    prev.next = head; #last node connects to head 

    p = head
    prev = None
    remain = n # number of nodes left in the list
    while remain >= 1:
        for i in range (1 , m):   # move every m-1 steps
            prev = p
            p = p.next		        
        prev.next = p.next # remove the mth node from the list 
        p = prev.next
        remain -= 1 
    return p.data

# test
n = 17
m = 3
p = last_man_standing(n, m)
print("last man standing: " + str(p))

