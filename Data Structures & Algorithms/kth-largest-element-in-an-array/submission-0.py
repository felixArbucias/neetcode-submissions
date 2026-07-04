class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)
        return res[-1]
        