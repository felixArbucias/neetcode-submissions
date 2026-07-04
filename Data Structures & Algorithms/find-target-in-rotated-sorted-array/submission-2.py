class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums)-1

        while L <= R:
            mid = (L+R) // 2 
            if nums[mid] == target:
                return mid 
            if nums[L] <= nums[mid]: # we are in the left portion
                if nums[L] > target or nums[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            else: # right portion
                if nums[mid] > target or nums[R] < target:
                    R = mid - 1 
                else:
                    L = mid + 1 
        return -1 