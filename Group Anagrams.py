def group_anagrams(strs):
    if not strs:
        return []
    anagrams_dict = {} # Key: sorted word Value: list of the original strings

    for word in strs:

        sorted_word = "".join(sorted(word))

        # if sorted word not availabe in dict
        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = []

        anagrams_dict[sorted_word].append(word)
    return list(anagrams_dict.values())



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))