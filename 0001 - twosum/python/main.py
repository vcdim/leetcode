from solution import Solution

sol = Solution()

res = sol.twoSum([2, 7, 11, 15], 9)
assert res == [0, 1], "Error!"

res = sol.twoSum([3, 2, 4], 6)
assert res == [1, 2], "Error!"

res = sol.twoSum([3, 3], 6)
assert res == [0, 1], "Error!"
