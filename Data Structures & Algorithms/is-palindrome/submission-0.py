class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch.lower() for ch in s if (ch.isalnum()))
        if s1[::-1] == s1:
            return True
        return False
        