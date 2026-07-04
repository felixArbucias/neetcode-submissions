class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1
        if len(nums) == 0:
            return 0 
        for n in nums:
            if n-1 not in nums:
                length = 1 
                temp = n+1
                while (n + length) in nums:
                    length +=1
                    if res < length:
                        res = length
        return res 