def convert_LC_to_UC(string):
    result = ""
    for s in string:
        if 'a' <= s <= 'z':
            result += chr(ord(s)-32)
        else:
            result += s
    return result



print(convert_LC_to_UC("a"))
print(convert_LC_to_UC("A"))
print(convert_LC_to_UC("HELLO"))
print(convert_LC_to_UC("Hello"))