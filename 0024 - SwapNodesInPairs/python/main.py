from solution import Solution
from listnode import MyList

sol = Solution()

res = sol.swapPairs(MyList([1,2,3,4]).head)
assert res.val == 2
assert res.next.val == 1
assert res.next.next.val == 4
assert res.next.next.next.val == 3
