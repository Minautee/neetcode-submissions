from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        nums_dict = {}
        nums_dict = Counter(nums)
        output = nums_dict.most_common(k)
        result = [x[0] for x in output]
        return result