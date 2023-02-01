from solution import Solution

sol = Solution()
res = sol.lengthOfLongestSubstring("abcabcbb")
assert res == 3
res = sol.lengthOfLongestSubstring("bbbbb")
assert res == 1
res = sol.lengthOfLongestSubstring("pwwkew")
assert res == 3

