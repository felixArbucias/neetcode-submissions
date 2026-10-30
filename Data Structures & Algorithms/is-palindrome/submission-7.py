class Solution:
    def isPalindrome(self, string: str) -> bool:
        newStr = []

        for c in string:
            if c.isalnum():
                newStr += c.lower()
            else:
                continue
        
        if newStr == newStr[::-1]:
            return True
        return False