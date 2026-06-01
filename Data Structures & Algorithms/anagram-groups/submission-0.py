from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use a defaultdict to handle missing keys automatically
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the string to create a unique key for all anagrams
            # 2. Join the list back into a string to use as a dictionary key
            sorted_key = "".join(sorted(s))
            
            # 3. Append the original word to the list associated with that key
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())
