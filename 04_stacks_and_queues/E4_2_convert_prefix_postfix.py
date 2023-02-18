my_stack = __import__('1_stack')

# Prefix to postfix, Time O(n), Space O(n), n is length of expression
def prefix_to_post(exp) :
    length = len(exp)		 
    stack = my_stack.Stack(length)  
    for i in range(length-1, -1, -1) :
        x = exp[i]
        if x not in ['+', '-', '*', '/'] :
            stack.push(x + " ");				
        else :			
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + x + " "
            stack.push(temp)
    return stack.top()

# Postfix to prefix, Time O(n), Space O(n), n is length of expression
def postfix_to_prefix(exp):
    length = len(exp)		 
    stack = my_stack.Stack(length)  
    for i in range(0, length) :
        x = exp[i]
        if x not in ['+', '-', '*', '/'] :
            stack.push(x + " ")
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            temp = x + " " + s2 + s1
            stack.push(temp)          
    return stack.top()

# Test
s =" + * 2 3 4"
s = s.strip().split(" ")
print("postfix: " + prefix_to_post(s))	

s="2 2 12 9 + 2 - + * "
s = s.strip().split(" ")
print("prefix: " + postfix_to_prefix(s))	