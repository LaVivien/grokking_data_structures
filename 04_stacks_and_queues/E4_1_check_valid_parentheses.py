my_stack = __import__('1_stack')

# Time O(n), Space O(n), n is length of input string
def isValid(s) :
    stack = my_stack.Stack(len(s))
    for c in s :
        if c not in ['(', ')', '[', ']', '{', '}'] : #skip others
            continue
        elif c == '(':
            stack.push(')')
        elif c == '{':
            stack.push('}')
        elif c == '[':
            stack.push(']')
        elif stack.is_empty() or stack.pop() != c:
            return False
    return stack.is_empty()

# Test
s = "{()}([{}])"				  
print("Is valid: "+ str(isValid(s)))

s = "((12+B)+{[k/s]}"				  
print("Is valid: "+ str(isValid(s)))