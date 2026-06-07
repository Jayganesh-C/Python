def alternator_str():
    input_string = input("Enter the string: ")
    result = []  # Use a list to collect the new characters
    
    for i in range(len(input_string)):
        char = input_string[i]
        
        if i % 2 == 0:
            # Even index: force to uppercase
            result.append(char.upper())
        else:
            # Odd index: force to lowercase
            result.append(char.lower())
            
    # Join the list of characters back into a single string
    return "".join(result)

print(alternator_str())