class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1

            while left < right:
                threeSum = nums[left] + nums[right] + a

                if threeSum > 0:
                    right -= 1
                
                if threeSum < 0:
                    left += 1
                
                if threeSum == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return res

