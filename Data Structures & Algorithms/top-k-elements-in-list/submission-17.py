class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1+count.get(n, 0)
        
        res = []
        for frequency, counter in count.items():
            freq[counter].append(frequency)
        
        for i in range(len(freq)-1, -1, -1):
            for r in freq[i]:
                res.append(r)
                if len(res) == k:
                    return res