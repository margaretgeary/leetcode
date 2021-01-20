# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1("ba").
# Example 2:

# Input: s1 = "ab" s2 = "eidboaoo"
# Output: False

#steps
#get all permutations of s1 --> we can do this by making s1 into a list (call it s1_list)
#check to see if s1_list[0] is in s2
# if it is, mark where in s2 it is located

from itertools import permutations

def find_permutation_in_string(s1, s2):
    from itertools import permutations
    perms = [''.join(p) for p in permutations(s1)]

    for perm in perms:
        if perm in s2:
            return True

    return False

print(find_permutation_in_string("ab", "eidbaooo"))
print(find_permutation_in_string("ab", "eidboaoo"))
print(find_permutation_in_string("ab", "baooooo"))
print(find_permutation_in_string("ab", "ajjjjjb"))

# if __name__ == '__main__': 
#     print(True == find_permutation_in_string("ab", "eidbaooo"))
#     print(False == find_permutation_in_string("ab", "eidboaoo"))
