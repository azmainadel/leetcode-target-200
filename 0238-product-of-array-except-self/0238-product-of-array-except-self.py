class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        preFixProduct = 1
        for i in range(len(nums)):
            res[i] = preFixProduct
            preFixProduct *= nums[i]
        
        postFixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postFixProduct
            postFixProduct *= nums[i]

        return res