class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        for i, u in enumerate(haystack):
            isMatch = True
            for j, v in enumerate(needle):
                if i+j > len(haystack)-1 or haystack[i+j] != v:
                    isMatch = False
                    break
            if isMatch:
                return i
        return -1