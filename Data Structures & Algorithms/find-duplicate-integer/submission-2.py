class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]
        return -1 