from solution import Solution
from listnode import MyList

sol = Solution()

res = sol.addTwoNumbers(MyList([2, 4, 3]).head, MyList([5, 6, 4]).head)
assert res.val == 7
assert res.next.val == 0
assert res.next.next.val == 8

res = sol.addTwoNumbers(MyList([0]).head, MyList([0]).head)
assert res.val == 0

res = sol.addTwoNumbers(MyList([9, 9, 9, 9, 9, 9, 9]).head, MyList([9, 9, 9, 9]).head)
assert res.val == 8
assert res.next.val == 9
assert res.next.next.val == 9
assert res.next.next.next.val == 9
assert res.next.next.next.next.val == 0
assert res.next.next.next.next.next.val == 0
assert res.next.next.next.next.next.next.val == 0
assert res.next.next.next.next.next.next.next.val == 1

