class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        topElement = None 
        count = 0
        for n in nums:
            if topElement == None:
                topElement = n
                count += 1 
            elif topElement == n:
                count +=1 
            elif count == 0: 
                topElement = n 
                count += 1
            else:
                count -=1 
        return topElement
            
