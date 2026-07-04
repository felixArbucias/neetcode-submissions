class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = 1
        prefix = 1
        res = [1] * len(nums)   

        for i in range(len(nums)): # this is the prefix
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1 # 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res 




        return res 
        # res = [1, 1, 2, 8] before the post fix 
        # postfix = 1
        #  [1, 1, 2, 8] after the post fix 