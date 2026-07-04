class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result, left = 0, 0 
        length = 0 
        for c in range(len(s)):
            if s[c] in charSet:
                while s[c] in charSet:

                    charSet.remove(s[left])
                    length -= 1 
                    result = max(result, length)
                    left += 1 
                charSet.add(s[c])
                length += 1 
                
                
            else:
                length += 1
                charSet.add(s[c])
                result = max(result, length)
        return result



