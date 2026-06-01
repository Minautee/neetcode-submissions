from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = 0
        string_1 = Counter(s)
        string_2 = Counter(t)
        if len(s) == len(t):
            for k1, v1 in string_1.items():
                if k1 in string_2.keys() and v1 in string_2.values():
                    anagram += 0
                else:
                    anagram += 1
            if anagram == 0:
                return True
        return False
        