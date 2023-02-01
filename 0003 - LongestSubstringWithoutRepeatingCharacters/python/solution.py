class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        ed = 0
        n = len(s)
        lenmax = 0
        for ed in range(n):
            sub_string = s[st:ed]
            c = s[ed]
            if c not in sub_string:
                ed += 1
            else:
                st = sub_string.rfind(c) + 1 + st
            lenmax = max(lenmax, ed-st)
        return lenmax