class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            # Example: "Hello" -> "5#Hello"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter to know where the length ends
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Extract the actual string based on the length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the pointer to the start of the next encoded block
            i = end
            
        return res
