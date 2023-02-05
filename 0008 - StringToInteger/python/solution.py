class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for u in s:
            current_digit = ord(u) - ord('0')
            if 0 > current_digit or current_digit > 9:
                break
            res *= 10
            res += current_digit
        res = res * sign
        if res < -2 ** 31:
            res = -2 ** 31
        if res > 2 ** 31 - 1:
            res = 2 ** 31 -1
        return res