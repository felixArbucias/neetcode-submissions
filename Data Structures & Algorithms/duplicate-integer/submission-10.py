class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setSeen = []
        for n in nums:
            if n in setSeen:
                return True
            setSeen.append(n)
        return False