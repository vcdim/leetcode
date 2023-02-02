import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        maxlen = 1
        result = s[0]

        m = 0
        for c in range(1, n):
            for l in range(min(c, n-c-1)+1):
                if s[c-l] == s[c+l]:
                    m = l
                else:
                    break
            if 2*m+1 > maxlen:
                result = s[c-m:c+m+1]
                maxlen = 2*m+1
            
        m = 0
        for c in np.arange(1/2, n+1/2):
            for l in np.arange(1/2, min(c, n-c-1)+1):
                if s[int(c-l)] == s[int(c+l)]:
                    m = l
                else:
                    break
            if 2*m+1 > maxlen:
                result = s[int(c-m):int(c+m+1)]
                maxlen = 2*m+1
        return result