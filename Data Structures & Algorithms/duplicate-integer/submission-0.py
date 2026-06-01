from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = Counter(nums)
        print(output)
        for k, v in output.items():
            if v > 1:
                return True
        return False

        