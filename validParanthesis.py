def isValid(s: str) -> bool:
    # Map each closing bracket to its corresponding opening bracket
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the top element from the stack if it's not empty; 
            # otherwise, assign a dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the top element, it's invalid
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0

# --- Test Cases ---
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
print(isValid("([)]"))     # Output: False
print(isValid("{[]}"))     # Output: True
print(isValid("{[]}"))     # Output: True



def isValidWithChar(s: str) -> bool:

    bracket_map = {"]": "[", "}": "{", ")": "("}
    stack = []

    open_brackets = set(bracket_map.values())
    close_brackets = set(bracket_map.keys())

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:

            top_char = stack.pop() if stack else "#"

            if top_char != bracket_map[char]:
                return False

    return len(stack) == 0

print("-----------Valid with characters------------")
print(isValidWithChar("{[aaa]}"))     # Output: True
print(isValidWithChar("d(ds)asdd"))       # Output: True
print(isValidWithChar("d()[d]{}"))   # Output: True
print(isValidWithChar("(d]"))       # Output: False
print(isValidWithChar("([d)]"))     # Output: False
print(isValidWithChar("{[d]}"))     # Output: True