s = "([{}]"

def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == pairs[char]:
                stack.pop(-1)
            else:
                return False

        
    return len(stack) == 0


print(is_balanced(s))
