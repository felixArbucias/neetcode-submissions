class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # track the frequency for the elemetn
        
        # hashmap to count the occurrences of each number in nums to frequency 
        # iterate through the hashmap to, storing each of these elements in an array
        # sort the array, return the top k frequented elements

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        arr = []
        for num, freq in count.items():
            arr.append([freq,num])
        arr.sort(reverse=True)
        result = []

        for i in range(k):
            result.append(arr[i][1])
        return result

