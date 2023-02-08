class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sgn = ((dividend < 0) == (divisor < 0))
        a = abs(dividend)
        b = abs(divisor)
        
        ans = 0
        
        while a >= b:
            q = 0
            while a > (b << (q+1)):
                q += 1
            ans += 1 << q
            a -= b << q
        
        if (ans == (1 << 31)) and sgn:
            return (1 << 31)-1
        
        if sgn:
            return ans
        else:
            return -ans