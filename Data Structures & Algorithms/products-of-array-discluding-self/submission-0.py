class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        suffix = []
        for i in range(len(nums)):
            prod_p = 1
            while i + 1 < len(nums):
                i += 1
                prod_p *= nums[i]
            prefix.append(prod_p)
            print(prefix)
        for j in range(len(nums) - 1, -1, -1):
            prod_s = 1
            while j - 1 >= 0:
                j -= 1
                print(j)
                prod_s *= nums[j]
            suffix.append(prod_s)
            print(suffix)
        for k in range(len(prefix)):
            product = prefix[k] * suffix[::-1][k]
            output.append(product)
            
        return output