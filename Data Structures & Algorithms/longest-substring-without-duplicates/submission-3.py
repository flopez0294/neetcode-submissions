class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest = ""
        currlong = 0
        maxlong = 0
        l = 0
        r = 0
        for idx, i in enumerate(s):
                
            
            while i in longest:
                longest = longest[1:]
                l += 1
            longest += i
            r = idx   
            if r - l + 1 > maxlong:
                maxlong = r - l + 1
        return maxlong
        
