class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = None
        for l in range(len(heights)):
          for r in range(l+1, len(heights)):
            area = min(heights[l],heights[r]) * (r-l)
            if res == None or area > res:
              res = area

        return res 