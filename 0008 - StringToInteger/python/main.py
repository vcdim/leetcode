from solution import Solution

sol = Solution()
res = sol.myAtoi("42")
assert res == 42
res = sol.myAtoi("+-12")
assert res == 0
