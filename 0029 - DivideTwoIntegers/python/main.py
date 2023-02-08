from solution import Solution

sol = Solution()
res = sol.divide(10, 3)
assert res == 3
res = sol.divide(-2**32, -1)
assert res == 2**32-1
