class Stack :

    # Constructor, Time O(1), Space O(1)
    def __init__(self, size) :
        self.top_index = -1
        self.stack = [None]*size
        self.max_size = size
       
    # Push at the top, Time O(1), Space O(1)
    def push(self, value):
        if self.is_full():
            print ("Reach max size, cannot add.")
            return
        self.top_index += 1   
        self.stack[self.top_index] = value
              
    # Remove from the top, Time O(1), Space O(1)
    def pop(self):
        if self.is_empty():
            print("stack is empty, cannot pop")
            return None   
        top_item = self.stack[self.top_index]
        self.top_index -= 1   
        return top_item

    # Return the top value, Time O(1), Space O(1)
    def top(self):
        if self.is_empty():
            print("stack is empty, no value return")
            return None 
        return self.stack[self.top_index] 
    
	# Print all, Time O(n), Space O(1), n is number of items in stack
    def print(self) :
        for i in range (self.top_index, -1, -1):
            print(self.stack[i], end= " ")
        print()
	
    # Return number of items in stack, Time O(1), Space O(1)
    def size(self) :
        return self.top_index + 1

    # Check empty, Time O(1), Space O(1)
    def is_empty(self):
        return self.top_index == -1

    # Check full, Time O(1), Space O(1)
    def is_full(self):
        return self.top_index == self.max_size -1

# test
if __name__ == '__main__':
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(80)
    stack.push(54)
    stack.push(60)
    stack.print()
    print("size: " + str(stack.size())) 
    print("top: " + str(stack.top()))

    stack.pop()
    stack.print()
    print("size: " + str(stack.size())) 
    print("top: " + str(stack.top()))

    stack.push(60)
    stack.print()
    print("is empty: " + str(stack.is_empty()))
    print("is full: " + str(stack.is_full()))