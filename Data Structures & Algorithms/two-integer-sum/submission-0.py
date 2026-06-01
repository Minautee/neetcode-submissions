class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums:
                j = nums.index(num)
                print(i, j)
                if (i not in output or j not in output) and i != j:
                    output.append(i)
                    output.append(j)
            output.sort()
        return output