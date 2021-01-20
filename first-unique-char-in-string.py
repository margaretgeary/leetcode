def find_first_unique_char(string):
    char_dict = {}
    for letter in string:
        char_dict[letter] = char_dict.get(letter, 0) +1
    for i, letter in enumerate(string):
        if char_dict[letter] == 1:
            return i
    return -1


print(find_first_unique_char("leetcode"))
print(find_first_unique_char("loveleetcode"))
print(find_first_unique_char("eeeeee"))
