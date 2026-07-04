class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = []

        for n in nums:
            if n in myset:
                return True 
            else:
                myset.append(n)
        if len(myset) == len(nums):
            return False 
                
    