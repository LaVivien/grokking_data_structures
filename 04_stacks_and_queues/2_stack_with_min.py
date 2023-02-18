class Node:
    # Constructor, Time O(1), Space O(1)
    def __init__(self, value, node = None):
        self.data = value
        self.min = value
        self.next = node

    # Override the print format, Time O(1), Space O(1)
    def __str__(self):
        return str(self.data) + "/" + str(self.min)+"(min)"

class Stack:
    # Constructor, Time O(1), Space O(1)
    def __init__(self):
        self.head = None
        self.stack_size = 0
    
    # Push at the top,Time O(1), Space O(1)
    def push(self, value):
        if self.head == None: 
            self.head = Node(value)
        else :
            new_node = Node(value, self.head)
            new_node.min = min(value, self.head.min)
            self.head = new_node
        self.stack_size += 1

    # Remove from the top, Time O(1), Space O(1)    
    def pop(self):
        if self.head == None:
            return None
        top_item = self.head
        self.head = self.head.next
        self.stack_size -= 1
        return top_item

    # Return the top value, Time O(1), Space O(1)
    def top(self):
        if self.head == None:
            return None
        return self.head 
    
    # Return the min value, Time O(1), Space O(1)
    def min(self):
        if self.head == None:
            return None
        return  self.head.min

    # Return number of items in stack, Time O(1), Space O(1)
    def size(self):
        return self.stack_size

    # Check empty, Time O(1), Space O(1)
    def is_empty(self):
        return self.stack_size == 0

    #print all, Time O(n), Space O(1), n is number of items in stack
    def print(self) :
        print ("stack: ", end='')
        curr = self.head
        while curr != None:
            print(str(curr.data), end = ' ')
            curr = curr.next
        print()

# test
if __name__ == '__main__':
    stack = Stack()
    stack.push(26)   
    stack.push(7)
    stack.push(10)
    print(stack.top())
    stack.push(44)
    stack.push(5)
    stack.print()
    print("smallest: " + str(stack.min()))
    print("size: " + str(stack.size()))

    print("\nPop one item:")
    stack.print()
    print("smallest: " + str(stack.min()))
    print(stack.pop())
    
    print("\nPush again:")
    stack.push(-3)
    stack.print()
    print("smallest: " + str( stack.min()))
    print("size: " + str(stack.size()))

    print("is empty: " + str(stack.is_empty()))
