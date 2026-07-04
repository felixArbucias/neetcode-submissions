class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                length = 1
                while (n+length) in numSet:
                    longest = max(longest, length)
                    length += 1 
            else:
                continue
        return longest + 1 

