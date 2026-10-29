class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setSeen = set()
        for n in nums:
            if n in setSeen:
                return True
            setSeen.add(n)
        return False