class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet =set(nums)
        resLen = 0
        for n in numSet:
            if n-1 not in numSet:
                length = 1
                while n+length in numSet:
                    length += 1

                resLen = max(resLen, length)
        return resLen