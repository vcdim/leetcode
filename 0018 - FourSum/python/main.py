from solution import Solution

sol = Solution()

res = sol.fourSum([1,0,-1,0,-2,2], 0)
assert res == [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]