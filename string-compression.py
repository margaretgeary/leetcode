def compress_string(list):
    result_string = ""
    char_dict = {}
    for letter in list:
        char_dict[letter] = char_dict.get(letter, 0) + 1
    for i, letter in enumerate(list):
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            if char_dict[letter] == 1:
                result_string += letter
                char_dict[letter] += 1
            else:
                result_string += letter
                result_string += str(char_dict[letter])
    return result_string


print(compress_string(["a", "a", "b", "b", "c", "c", "c"]))
print(compress_string(["a"]))
print(compress_string(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(compress_string(["a", "a", "a", "b", "b", "a", "a"]))
