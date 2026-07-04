class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)

        if len(res) == len(nums):
            return False
        return True 
    