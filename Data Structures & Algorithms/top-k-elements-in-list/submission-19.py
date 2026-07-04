class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for n in nums:
            cache[n] = 1 + cache.get(n, 0)
        
        for i, v in cache.items():
            freq[v].append(i)
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
                