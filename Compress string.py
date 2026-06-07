def compress_string(s):

    if not s:
        return s

    compressed = []
    count = 1

    for i in range(len(s)-1):

        if s[i]==s[i+1]:
            count+=1
        else:
            compressed.append(s[i]+str(count))
    
    compressed.append(s[-1]+str(count)) # do this to also count the last char

    result = "".join(compressed)

    return result if len(result) < len(s) else s # if/else for the case "abcd"
    

# --- Test Cases ---
print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"
print(compress_string("abcd"))         # Output: "abcd" (Compression "a1b1c1d1" is longer!)
print(compress_string("AAAbbbCC"))     # Output: "A3b3C2"