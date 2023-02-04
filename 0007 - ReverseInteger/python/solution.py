class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        if x < 0:
            sgn = -1
            x = -x   
        else:
            sgn = 1

        s = r = x % 10
        q = x // 10
        while q > 0:
            s *= 10
            s += q % 10
            q = q // 10
        res = s * sgn
        if res > 2**31 -1 or res < -2**31:
            return 0
        return res