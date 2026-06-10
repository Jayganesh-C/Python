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