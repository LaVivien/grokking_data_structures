# Write a class to construct a doubly linked list from an input string or number. 
# Check whether the input is a palindrome.

class DllNode: 
	# Constructor, Time O(1), Space O(1)
    def __init__(self, value): 
        self.data = value
        self.next = None
        self.pre = None

class CheckPalindromeDll:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.head = None
        self.tail = None

    # Create a new linked list from the input, Time O(n), Space O(n)
    def input_to_list(self, input):
        self.head = None # a new input
        self.tail = None
        for c in str(input):
            newNode = DllNode(c)
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                newNode.pre = self.tail
                self.tail = newNode

    # Check parlindrom, Time O(n), Space O(1)
    def is_palindrome(self) :
        if self.head == None:
            return False       
        left = self.head
        right = self.tail
        while left != right:    
            if left.data != right.data:
                return False
            left = left.next
            right = right.pre          
        return True

    # Print list, Time O(n), Space O(1)
    def display(self):
        p = self.head
        while p != None:
            print(p.data, end='')
            p = p.next
        print()

#test
dll = CheckPalindromeDll()
dll.input_to_list("level")
dll.display()
print(dll.is_palindrome())

dll.input_to_list(1234)
dll.display()
print(dll.is_palindrome())
