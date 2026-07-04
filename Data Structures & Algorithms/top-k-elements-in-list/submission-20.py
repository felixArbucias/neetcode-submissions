class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums: # adding 1 to the frequency every time we see a value
            hashmap[n] = 1 + hashmap.get(n, 0) 

        for key, frequency in hashmap.items(): # bucket sort based on frequency of values 
            freq[frequency].append(key)

        res = []
        for i in range(len(freq)-1, -1, -1): # decrementing backwards to get highest frequency values
            for n in freq[i]: # iterate through each bucket, appending value to result array
                res.append(n)
                if len(res) == k: # if we have k elements, return k 
                    return res 
                
        















