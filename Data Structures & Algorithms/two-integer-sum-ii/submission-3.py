class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        last = len(numbers)-1 
        while l < last:
            r = len(numbers)-1
            for i in range(len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                else:
                    r -= 1 
            l += 1 
            