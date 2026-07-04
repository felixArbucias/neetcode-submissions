class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if n in res:
                return n 
            res.append(n)
        return -1