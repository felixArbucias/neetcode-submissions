class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l, r, res = 1, max(piles), max(piles)
       while l <= r: 
        time = 0
        m = (l+r) // 2 

        for p in piles:
            time += math.ceil(float(p) / m)
            
        if time <= h:
            res = m
            r = m - 1 
        else:
            l = m + 1 
       return res 
    
