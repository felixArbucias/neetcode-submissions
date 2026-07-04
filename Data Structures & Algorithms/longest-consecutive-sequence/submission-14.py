class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
          return 0
        nums = set(nums)
        res = 1
        for n in nums:
          length = 1 
          if n - 1 not in nums:
            while (n+length) in nums:
              length += 1 
              res = max(res, length)
        return res 

