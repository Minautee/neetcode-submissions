class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "}": "{", "]":"["}
        stack = []

        for ch in s:
            if ch in parentheses:
                if stack and parentheses[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        if not stack:
            return True
        return False
        