class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        
        preFixProduct = 1
        for i in range(len(nums)):
            pre[i] = preFixProduct
            preFixProduct *= nums[i]

        postFixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = postFixProduct
            postFixProduct *= nums[i]

        return [pre[i]*post[i] for i in range(len(pre))]