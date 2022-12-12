# Write a function to add two numbers stored in two linked lists.

class Node :  	 
	#Constructor, Time O(1), Space O(1)
    def __init__(self, value, nextNode = None):
        self.data = value
        self.next = nextNode	

# Store a number is a linked list, the last digit is head, Time O(n), Space O(n)
# n is number of digits
def num_to_List(num):
    head = None
    for d in str(num):
        head = Node(int(d), head)
    return head

# Add two numbers stored in two linked lists, The result is in a new list, 
# Time O(n), Space O(n)
def add_two_numbers(a, b):
    newHead = Node(0)
    p = newHead 
    sum = 0
    while a != None or b != None:
        if a != None:
            sum += a.data
            a = a.next
        if b != None: 
            sum += b.data
            b = b.next
        p.next = Node(int(sum % 10))
        p = p.next
        sum = int(sum / 10)
    if sum == 1: 
        p.next = Node(1)	
    return newHead.next

# Print from the end to head, Time O(n), Space O(n)
def print_from_end(head):	
    if head == None:
        return
    print_from_end(head.next)
    print(head.data,  end = '')

# test
# put 213 in list1, 3 in head
head1 = num_to_List (213)

# put 369 in list2, 9 is head
head2 = num_to_List(369)

# the last digit in the number is in head
result = add_two_numbers(head1, head2)
print_from_end(result) # print from the first digit in the number
	